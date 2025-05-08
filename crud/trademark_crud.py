import json
from typing import List, Optional
from pathlib import Path
from schemas.trademark_schema import Trademark
from rapidfuzz import fuzz, process

DATA_PATH = Path("data/trademark_sample.json")

# JSON 파일을 한번만 읽어 Pydantic 모델 리스트로 반환
with open(DATA_PATH, "r", encoding="utf-8") as f:
    raw_data = json.load(f)
    _DATA = [Trademark(**item) for item in raw_data]

with open("data/product_name_to_code.json", "r", encoding="utf-8") as f:
    product_name_to_code = json.load(f)

def load_data() -> List[Trademark]:
    return _DATA

# 페이징
def paginate(data: List[Trademark], skip: int, limit: int) -> List[Trademark]:
    return data[skip : skip + limit]

# 상표명으로 검색
def search_by_product_name(name: str, skip: int = 0, limit: int = 10) -> List[Trademark]:
    data = load_data()
    
    # 유사도가 70이상이면 포함 + 영문, 한글 둘다 가능
    filtered = [
        item for item in data
        if (
            item.productName and fuzz.partial_ratio(name, item.productName) > 70
        ) or (
            item.productNameEng and fuzz.partial_ratio(name, item.productNameEng) > 70
        )
    ]
    return paginate(filtered, skip, limit)


# 등록상태로 검색
def search_by_register_status(status: str, skip: int = 0, limit: int = 10) -> List[Trademark]:
    data = load_data()
    
    filtered = [
        item for item in data
        if item.registerStatus and status.lower() in item.registerStatus.lower()
    ]
    return paginate(filtered, skip, limit)


# 출원번호로 검색
def search_by_application_number(application_number: str, skip: int = 0, limit: int = 10) -> List[Trademark]:
    data = load_data()
    
    filtered = [
        item for item in data
        if item.applicationNumber == application_number
    ]
    return paginate(filtered, skip, limit)

# 상품명칭 -> 분류코드 변환
def resolve_product_code(user_input: str) -> Optional[str]:
    # 사용자가 코드 자체를 입력한 경우
    try:
        int_val = int(user_input)
        return str(int_val).zfill(2)
    except ValueError:
        pass

    # 유사도 기반 상품명 검색
    result = process.extractOne(user_input, product_name_to_code.keys())
    if result:
        match, score, _ = result
        if score >= 80:
            code = product_name_to_code[match]
            return code.zfill(2)

    return None

# 상품 코드 및 상품명 검색 (상품명 입력시 상품 코드로 변환해서 적용)
def search_by_product_main_code(user_input: str, skip: int = 0, limit: int = 10) -> List[Trademark]:
    code = resolve_product_code(user_input)
    if not code:
        return []

    data = load_data()
    filtered = [
        item for item in data
        if item.asignProductMainCodeList and code in item.asignProductMainCodeList
    ]
    return paginate(filtered, skip, limit)

import pandas as pd
import json

# 엑셀 파일 경로
excel_path = "data/특허청 고시상품명칭.xlsx"

# 엑셀 파일 읽기
df = pd.read_excel(excel_path, dtype=str)

# 중복 제거 + 매핑 딕셔너리 생성
mapping = df.drop_duplicates(subset=["지정상품(국문)"]) \
            .set_index("지정상품(국문)")["NICE분류"] \
            .to_dict()

# JSON 저장 경로
json_path = "data/product_name_to_code.json"

# JSON 저장
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(mapping, f, ensure_ascii=False, indent=2)

print(f"저장 완료: {json_path}")

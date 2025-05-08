from fastapi import APIRouter, Query
from typing import List
from schemas.trademark_schema import Trademark
from crud import trademark_crud

router = APIRouter(
    prefix="/trademarks",
    tags=["Trademarks"]
)

# 상표명 검색 API
@router.get("/search/name", response_model=List[Trademark])
def search_by_product_name(
    name: str = Query(..., description="상표명을 입력하세요"),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1)):
    return trademark_crud.search_by_product_name(name, skip, limit)

# 등록 상태 검색 API
@router.get("/search/status", response_model=List[Trademark])
def search_by_register_status(
    status: str = Query(..., description="등록상태 (예: 등록, 실효, 거절, 출원 등)"),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1)):
    return trademark_crud.search_by_register_status(status, skip, limit)

# 출원번호 검색 API
@router.get("/search/application-number", response_model=List[Trademark])
def search_by_application_number(
    application_number: str = Query(..., description="정확한 출원번호 입력"),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1)):
    return trademark_crud.search_by_application_number(application_number, skip, limit)

# 상품 코드 및 상품명 검색 API
@router.get("/search/main-code", response_model=List[Trademark])
def search_by_product_main_code(
    input: str = Query(..., description="상품 코드 입력 및 한글 상품명 입력 (예: 화장품, 의류 등)"),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1)
):
    return trademark_crud.search_by_product_main_code(input, skip, limit)
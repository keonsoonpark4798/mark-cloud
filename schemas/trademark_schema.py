from typing import List, Optional
from pydantic import BaseModel

class Trademark(BaseModel):
    productName: Optional[str]                              # 상표명
    productNameEng: Optional[str]                           # 상표명(영문)
    applicationNumber: Optional[str]                        # 출원번호
    applicationDate: Optional[str]                          # 출원일
    registerStatus: Optional[str]                           # 상표 등록 상태(등록, 실효, 거절, 출원 등)
    publicationNumber: Optional[str]                        # 공고번호
    publicationDate: Optional[str]                          # 공고일
    registrationNumber: Optional[List[Optional[str]]]       # 등록번호
    registrationDate: Optional[List[Optional[str]]]         # 등록일
    registrationPubNumber: Optional[str]                    # 등록공고번호
    registrationPubDate: Optional[str]                      # 등록일
    internationalRegDate: Optional[str]                     # 국제출원일
    internationalRegNumbers: Optional[str]                  # 국제 출원 번호
    priorityClaimNumList: Optional[List[Optional[str]]]     # 우선권 번호
    priorityClaimDateList: Optional[List[Optional[str]]]    # 우선권 일자 리스트
    asignProductMainCodeList: Optional[List[Optional[str]]] # 상품 주 분류 코드 리스트
    asignProductSubCodeList: Optional[List[Optional[str]]]  # 상품 유사군 코드 리스트
    viennaCodeList: Optional[List[Optional[str]]]           # 비엔나 코드 리스트

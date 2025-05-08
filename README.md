# 📘 MarkCloud 상표 검색 API 과제

FastAPI 기반으로 구현한 상표 검색 API입니다.

---

## 실행 방법

```bash
# 특허청 고시상품명칭 데이터 다운로드
https://www.kipo.go.kr/ko/kpoContentView.do?menuCd=SCD0201120

# 엑셀파일을 data 폴더에 넣고 createJSON으로 JSON 파일 생성
python createJSON.py

# 필수 라이브러리 설치
pip install -r requirements.txt

# 서버 실행
uvicorn main:app --reload
```

- 실행 후 Swagger 문서 확인: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 구현된 주요 기능

### 1. 상표명 기반 유사 검색

- **엔드포인트**: `/trademarks/search/name`
- 한글/영문 상표명에 대해 RapidFuzz로 유사도 기반 검색을 수행합니다.

### 2. 등록 상태 필터링

- **엔드포인트**: `/trademarks/search/status`
- 등록, 거절, 무효 등 등록 상태에 따라 필터링할 수 있습니다.

### 3. 출원번호로 검색

- **엔드포인트**: `/trademarks/search/application-number`
- 일치하는 출원번호가 있는 상표만 반환합니다.

### 4. 상품코드 및 상품명 검색색

- **엔드포인트**: `/trademarks/search/product-code`
- `asignProductMainCodeList` 필드에 지정된 코드가 포함된 상표만 반환합니다.

---

## 기술적 의사결정에 대한 설명

### 데이터 로딩 방식

- JSON 파일을 FastAPI 앱 실행 시 단 한 번만 메모리에 로딩하여 재사용합니다. 이는 불필요한 디스크 I/O를 줄이고 성능을 향상시킵니다.

### 검색 정확도와 유사도 대응

- `RapidFuzz`를 사용해 상표명과 상품명에 대한 부분 일치 및 오타 대응 검색을 구현했습니다.
- 한글 상품명과 코드 간 매핑 또한 유사도 기반으로 판단하도록 하여 사용자 입력의 자유도를 높였습니다.

### 성능 최적화

- JSON 데이터 전체를 메모리에 보관하고 있으며, `skip`, `limit` 파라미터를 통해 페이징 처리해 대량 데이터 대응을 고려했습니다.

### 유연한 사용자 입력 처리

- 상품명을 입력하든, 상품코드를 입력하든 동일한 API(/by-korean-product) 하나로 처리되도록 설계했습니다.

- 코드 입력 시 "9"/"09" 같은 형식을 자동 정규화(zfill(2))하여 비교 오류를 방지했습니다.

---

## 문제 해결 과정에서 고민했던 점

- 상품코드 `09` vs `9`의 형식 불일치로 필터링 실패 문제 발생

  > zfill(2)로 0을 채워서 자릿수를 맞춰 해결

- JSON을 매 요청마다 읽는 구조는 느리고 비효율적이라 판단
  > 서버 구동 시 1회 캐싱 방식으로 최적화

---

## 개선하고 싶은 부분

- 초성으로도 검색 가능하게 기능 추가

- 현재는 json 파일로 데이터를 받지만 DB로 이관해서 검색 더 용이하게

---

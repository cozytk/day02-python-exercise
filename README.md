# Day 02 실습: Python 데이터 처리 기초

## 🎯 이 실습을 완료하면?

이 실습을 통해 다음 역량을 갖추게 됩니다:

| 배우는 것 | 실무 활용 |
|----------|----------|
| 파일 I/O (텍스트, CSV, JSON) | 로그 파일 분석, 데이터 수집 |
| 데이터 변환 (CSV ↔ JSON) | API 연동, 데이터 포맷 변환 |
| 필터링, 그룹화, 통계 | 데이터 분석 리포트 생성 |
| **ETL 파이프라인** | 데이터 엔지니어링 핵심 역량 |

> 💡 **ETL이란?** Extract(추출) → Transform(변환) → Load(적재). 데이터 엔지니어의 핵심 업무!

---

## 📚 사전 준비

Day01 실습을 완료했다면 Git과 Docker가 이미 설치되어 있습니다.

```bash
# 확인
git --version
docker --version
```

> ⚠️ **중요**: Docker Desktop이 **실행 중**이어야 합니다!

---

## 🚀 Step by Step 실습 가이드

### Step 1: 저장소 Fork하기

1. GitHub에서 이 저장소 페이지로 이동
2. 오른쪽 상단의 **Fork** 버튼 클릭
3. "Create fork" 클릭

### Step 2: 로컬에 Clone하기

```bash
# YOUR_USERNAME을 본인의 GitHub 사용자명으로 변경
git clone https://github.com/YOUR_USERNAME/day02-python-exercise.git
cd day02-python-exercise
```

### Step 3: 현재 상태 확인 (모든 테스트 실패!)

```bash
docker compose run --rm test
```

25개 테스트가 모두 **FAILED**로 나오는 것이 정상입니다!

### Step 4: Part 1 - 파일 I/O 구현하기

먼저 가장 기본적인 텍스트 파일 읽기부터 시작합니다:

```python
def read_text_file(file_path: str) -> str:
    # TODO: open()과 read()를 사용하여 파일 내용 읽기
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
```

테스트:
```bash
docker compose run --rm test pytest test_exercise.py::TestReadTextFile -v
```

### Step 5: 단계별 구현하기

| 순서 | 함수명 | 테스트 명령어 |
|------|--------|-------------|
| **Part 1: 파일 I/O** | | |
| 1 | `read_text_file` | `pytest test_exercise.py::TestReadTextFile -v` |
| 2 | `write_text_file` | `pytest test_exercise.py::TestWriteTextFile -v` |
| 3 | `read_csv_as_dicts` | `pytest test_exercise.py::TestReadCsvAsDicts -v` |
| 4 | `write_dicts_to_csv` | `pytest test_exercise.py::TestWriteDictsToCsv -v` |
| 5 | `read_json_file` | `pytest test_exercise.py::TestReadJsonFile -v` |
| 6 | `write_json_file` | `pytest test_exercise.py::TestWriteJsonFile -v` |
| **Part 2: 데이터 변환** | | |
| 7 | `csv_to_json` | `pytest test_exercise.py::TestCsvToJson -v` |
| 8 | `json_to_csv` | `pytest test_exercise.py::TestJsonToCsv -v` |
| **Part 3: 데이터 처리** | | |
| 9 | `filter_by_condition` | `pytest test_exercise.py::TestFilterByCondition -v` |
| 10 | `group_and_count` | `pytest test_exercise.py::TestGroupAndCount -v` |
| 11 | `calculate_statistics` | `pytest test_exercise.py::TestCalculateStatistics -v` |
| **Part 4: ETL** | | |
| 12 | `simple_etl` | `pytest test_exercise.py::TestSimpleEtl -v` |

> 💡 테스트 명령어 앞에 `docker compose run --rm test`를 붙여서 실행하세요!

### Step 6: 전체 테스트 통과 확인

```bash
docker compose run --rm test
```

**25 passed**가 나오면 성공!

### Step 7: GitHub에 Push하기

```bash
git add .
git commit -m "feat: 모든 함수 구현 완료"
git push origin main
```

### Step 8: GitHub Actions 확인하기

GitHub Actions에서 녹색 체크마크(✅)가 보이면 **실습 완료!**

---

## 💡 막혔을 때는?

각 단계별로 정답이 포함된 브랜치가 준비되어 있습니다:

| 브랜치 | 포함된 함수 |
|--------|-----------|
| `base` | 빈칸 상태 (시작점) |
| `step-1` | Part 1: 파일 I/O (6개) |
| `step-2` | + Part 2: 데이터 변환 (2개) |
| `step-3` | + Part 3: 데이터 처리 (3개) |
| `step-4` | + Part 4: ETL (1개) |
| `main` | 모든 함수 완성 |

### 정답 확인 방법

```bash
# step-1에서 추가된 코드 확인
git diff base step-1 -- exercise.py

# 해당 브랜치로 전환해서 코드 확인
git checkout step-1
cat exercise.py

# 다시 원래 브랜치로
git checkout main
```

---

## 📝 주요 개념 힌트

### 파일 읽기/쓰기 패턴

```python
# 텍스트 파일 읽기
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# CSV 읽기
import csv
with open(path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# JSON 읽기
import json
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
```

### ETL 파이프라인

```python
def simple_etl(input_path, output_path, filter_key, filter_value):
    # 1. Extract: 데이터 추출
    data = read_json_file(input_path)

    # 2. Transform: 데이터 변환/필터링
    filtered = filter_by_condition(data, filter_key, filter_value)

    # 3. Load: 결과 저장
    write_json_file(output_path, filtered)
```

---

## 🐳 Docker 명령어 모음

| 명령어 | 설명 |
|--------|------|
| `docker compose run --rm test` | 전체 테스트 실행 |
| `docker compose run --rm test pytest test_exercise.py::TestXXX -v` | 특정 테스트만 실행 |
| `docker compose run --rm shell` | Python 대화형 셸 (디버깅용) |
| `docker compose build --no-cache` | 이미지 다시 빌드 |

---

## ⚠️ 자주 발생하는 오류

### "FileNotFoundError"

**원인**: 파일 경로가 잘못되었거나 파일이 없음

**해결**: 테스트에서 전달하는 경로를 그대로 사용하세요. 테스트가 임시 파일을 생성합니다.

### "UnicodeDecodeError"

**원인**: 파일 인코딩 문제

**해결**: `encoding='utf-8'` 옵션을 open()에 추가하세요.

```python
with open(path, 'r', encoding='utf-8') as f:
    ...
```

### JSON 관련 에러

**원인**: JSON 형식이 올바르지 않음

**해결**:
- `json.dump()` 사용 시 `ensure_ascii=False` 추가 (한글 지원)
- 딕셔너리 리스트인지 확인

```python
json.dump(data, f, ensure_ascii=False, indent=2)
```

### CSV 관련 에러

**원인**: CSV 헤더나 필드 불일치

**해결**:
- `csv.DictReader`와 `csv.DictWriter` 사용
- `fieldnames` 파라미터 확인

---

## 📁 파일 구조

```
day02-python-exercise/
├── README.md              # 이 파일 (실습 가이드)
├── exercise.py            # 🎯 빈칸 채우기 대상
├── test_exercise.py       # 테스트 코드 (수정 금지)
├── requirements.txt       # Python 패키지 목록
├── Dockerfile             # Docker 이미지 설정
├── docker-compose.yml     # Docker 서비스 설정
├── .dockerignore          # Docker 빌드 제외 파일
├── .gitignore             # Git 무시 파일
└── .github/
    └── workflows/
        └── test.yml       # GitHub Actions 설정
```

---

## 🎉 실습 완료 체크리스트

- [ ] 모든 25개 테스트 통과 (`docker compose run --rm test`)
- [ ] GitHub에 Push 완료 (`git push origin main`)
- [ ] GitHub Actions에서 녹색 체크마크(✅) 확인

**Day 02 완료! 내일은 SQL 기초를 배웁니다.** 🚀

# Python 학습 로드맵

파이썬 기초 문법부터 데이터 사이언스 라이브러리(pandas, matplotlib, Scikit-learn)까지
**예제 중심으로 따라 하며 배우는** 학습 계획입니다.

---

## 🌐 웹에서 바로 학습하기 (Python Quest)

**설치 없이 브라우저에서 바로 파이썬을 학습하세요!**

👉 GitHub Pages에서 배포된 웹 앱에 접속하면:
- 왼쪽 패널에서 **학습 내용**을 읽고
- 오른쪽 **코드 에디터**에서 직접 코드를 작성하고
- 하단 **터미널**에서 실행 결과를 즉시 확인할 수 있습니다

게임처럼 XP와 레벨 시스템으로 학습 진행도를 추적합니다!

> **로컬에서 실행**: `python3 -m http.server 8080 --directory web` 후 http://localhost:8080 접속

---

## 학습 방법

1. 각 챕터의 `.py` 파일을 **위에서 아래로 읽으며** 실행해 보세요.
2. 주석으로 설명이 달려 있으니, 코드를 **직접 수정**하며 결과를 확인해 보세요.
3. 각 파일 하단의 **연습 문제**를 직접 풀어 보세요.
4. `playground.py` **연습장**에서 자유롭게 코드를 작성하고 실험해 보세요.

## 실행 방법 (학습 도구)

### 방법 1: 학습 실행 도구 (`run.py`) 사용

```bash
python run.py              # 연습장(playground.py) 실행
python run.py play         # 연습장(playground.py) 실행
python run.py 1            # ch01 챕터 실행
python run.py ch05         # ch05 챕터 실행
python run.py list         # 전체 챕터 목록 보기
python run.py all          # 모든 챕터 순서대로 실행
python run.py help         # 도움말 보기
```

### 방법 2: Cursor/VSCode 단축키

| 단축키 | 동작 |
|--------|------|
| `Cmd+Shift+B` | 현재 열린 파일 바로 실행 |
| `F5` | 디버그 모드로 실행 (중단점 사용 가능) |

### 방법 3: 직접 실행

```bash
python 파일명.py           # 예: python part1_basics/ch01_hello.py
```

---

## Part 1. 파이썬 기초 (part1_basics/)

| 순서 | 파일 | 주제 | 핵심 내용 |
|------|------|------|-----------|
| 01 | `ch01_hello.py` | 첫 프로그램 & 변수 | print, 변수, input, 주석 |
| 02 | `ch02_data_types.py` | 자료형 | int, float, str, bool, type() |
| 03 | `ch03_operators.py` | 연산자 | 산술, 비교, 논리, 할당 연산자 |
| 04 | `ch04_strings.py` | 문자열 다루기 | 인덱싱, 슬라이싱, 메서드, f-string |
| 05 | `ch05_conditions.py` | 조건문 | if, elif, else, 중첩 조건 |
| 06 | `ch06_loops.py` | 반복문 | for, while, break, continue, range |
| 07 | `ch07_lists.py` | 리스트 | 생성, 인덱싱, 메서드, 정렬 |
| 08 | `ch08_tuples_sets.py` | 튜플 & 셋 | 불변성, 집합 연산 |
| 09 | `ch09_dicts.py` | 딕셔너리 | key-value, 메서드, 순회 |
| 10 | `ch10_functions.py` | 함수 | def, return, 매개변수, 기본값, *args, **kwargs |

## Part 2. 파이썬 중급 (part2_intermediate/)

| 순서 | 파일 | 주제 | 핵심 내용 |
|------|------|------|-----------|
| 11 | `ch11_file_io.py` | 파일 입출력 | open, read, write, with문 |
| 12 | `ch12_error_handling.py` | 예외 처리 | try, except, finally, raise |
| 13 | `ch13_classes.py` | 클래스 & OOP | class, __init__, 상속, 메서드 |
| 14 | `ch14_comprehension.py` | 컴프리헨션 & 람다 | 리스트/딕트 컴프리헨션, lambda, map, filter |
| 15 | `ch15_modules.py` | 모듈 & 패키지 | import, 표준 라이브러리, pip |

## Part 3. 데이터 사이언스 (part3_data_science/)

| 순서 | 파일 | 주제 | 핵심 내용 |
|------|------|------|-----------|
| 16 | `ch16_pandas_basics.py` | pandas 기초 | Series, DataFrame, 읽기/쓰기 |
| 17 | `ch17_pandas_manipulation.py` | pandas 데이터 가공 | 필터링, 그룹화, 결측치, 병합 |
| 18 | `ch18_matplotlib_basics.py` | matplotlib 기초 | 선 그래프, 막대 그래프, 산점도 |
| 19 | `ch19_matplotlib_advanced.py` | matplotlib 심화 | 서브플롯, 스타일, 저장 |
| 20 | `ch20_sklearn_basics.py` | Scikit-learn 기초 | 데이터셋, 전처리, train/test split |
| 21 | `ch21_sklearn_project.py` | Scikit-learn 실전 | 분류, 회귀, 모델 평가, 파이프라인 |

---

## 예상 학습 기간

| 파트 | 예상 기간 | 비고 |
|------|-----------|------|
| Part 1 기초 | 1~2주 | 하루 1~2챕터 |
| Part 2 중급 | 1주 | 하루 1챕터 |
| Part 3 데이터 사이언스 | 1~2주 | 하루 1챕터 + 복습 |
| **합계** | **약 3~5주** | 개인 속도에 따라 조정 |

---

## 환경 설정

```bash
# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # macOS/Linux

# 패키지 설치 (Part 3용)
pip install -r requirements.txt
```

---

> **Tip**: 모르는 것이 있으면 `help(함수명)` 또는 `dir(객체)` 를 활용해 보세요!

"""
Chapter 15: 모듈 & 패키지 (Modules & Packages)
=================================================
코드 재사용과 구조화를 위한 모듈 시스템을 배웁니다.
"""

# ============================================================
# JavaScript vs Python 비교 - 모듈
# ============================================================
#
#  JavaScript (ES Modules)              Python
#  ─────────────────────────────────   ─────────────────────────────
#  import math from 'math'             import math
#  import { sqrt, pi } from 'math'     from math import sqrt, pi
#  import * as math from 'math'        import math  (기본이 네임스페이스)
#  import m from 'math'                import math as m
#  export function foo() {}            (자동 - 모든 함수가 import 가능)
#  export default class {}             (없음 - __all__로 제어)
#  npm install 패키지명                 pip install 패키지명
#  package.json                         requirements.txt
#  node_modules/                        venv/lib/
#
#  핵심 차이:
#  1) Python은 export 키워드가 없음 (모든 것이 기본 export)
#  2) npm → pip, package.json → requirements.txt
#  3) node_modules → 가상환경(venv)
#  4) Python 표준 라이브러리가 훨씬 풍부 (batteries included!)
#     - JS: lodash, moment, csv-parser 등 외부 패키지 필요
#     - Python: collections, datetime, csv 등 내장!
#

# ============================================================
# 1. 모듈 import 기초
# ============================================================
print("=== import 기초 ===")

# 전체 모듈 가져오기
import math

print(f"math.pi = {math.pi}")
print(f"math.e = {math.e}")
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"math.ceil(3.2) = {math.ceil(3.2)}")
print(f"math.floor(3.8) = {math.floor(3.8)}")

print()


# ============================================================
# 2. 다양한 import 방식
# ============================================================
print("=== import 방식 ===")

# from ... import ... (특정 항목만)
# JS: import { sqrt, pi } from 'math'
from math import sqrt, pi
print(f"sqrt(25) = {sqrt(25)}")
print(f"pi = {pi}")

# 별칭 사용 (alias)
# JS: import * as m from 'math'
import math as m
print(f"m.pow(2, 10) = {m.pow(2, 10)}")

# from ... import * (권장하지 않음 - 이름 충돌 가능)
# from math import *

print()


# ============================================================
# 3. 주요 표준 라이브러리 - math
# ============================================================
print("=== math 모듈 ===")

import math

print(f"math.pi      = {math.pi}")
print(f"math.e       = {math.e}")
print(f"math.inf     = {math.inf}")
print(f"math.sqrt(2) = {math.sqrt(2):.4f}")
print(f"math.pow(2, 8)= {math.pow(2, 8)}")
print(f"math.log(100) = {math.log(100):.4f}")       # 자연로그
print(f"math.log10(100)= {math.log10(100)}")          # 상용로그
print(f"math.factorial(10) = {math.factorial(10)}")
print(f"math.gcd(12, 8) = {math.gcd(12, 8)}")        # 최대공약수

print()


# ============================================================
# 4. random 모듈
# ============================================================
print("=== random 모듈 ===")

import random

# random.random(): 0~1 사이 실수
print(f"random(): {random.random():.4f}")

# random.randint(a, b): a~b 사이 정수
print(f"randint(1, 10): {random.randint(1, 10)}")

# random.choice(): 리스트에서 하나 선택
fruits = ["사과", "바나나", "딸기", "포도", "수박"]
print(f"choice: {random.choice(fruits)}")

# random.sample(): 여러 개 선택 (중복 없이)
print(f"sample(3): {random.sample(fruits, 3)}")

# random.shuffle(): 섞기 (원본 변경)
numbers = list(range(1, 6))
random.shuffle(numbers)
print(f"shuffle: {numbers}")

# random.uniform(): 범위 내 실수
print(f"uniform(1, 10): {random.uniform(1, 10):.2f}")

# 재현 가능한 랜덤 (seed)
random.seed(42)
print(f"seed(42) → randint: {random.randint(1, 100)}")
random.seed(42)
print(f"seed(42) → randint: {random.randint(1, 100)}")  # 같은 값!

print()


# ============================================================
# 5. datetime 모듈
# ============================================================
print("=== datetime 모듈 ===")

from datetime import datetime, date, timedelta

# 현재 날짜/시간
now = datetime.now()
print(f"현재: {now}")
print(f"날짜: {now.date()}")
print(f"시간: {now.time()}")

# 날짜 포매팅
print(f"포맷: {now.strftime('%Y년 %m월 %d일 %H:%M:%S')}")
print(f"요일: {now.strftime('%A')}")

# 날짜 파싱
parsed = datetime.strptime("2025-12-25", "%Y-%m-%d")
print(f"파싱: {parsed}")

# 날짜 연산
today = date.today()
christmas = date(2025, 12, 25)
delta = christmas - today
print(f"\n오늘: {today}")
print(f"크리스마스까지: {delta.days}일")

# timedelta: 날짜 더하기/빼기
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(weeks=1)
print(f"내일: {tomorrow}")
print(f"지난주: {last_week}")

print()


# ============================================================
# 6. collections 모듈
# ============================================================
print("=== collections 모듈 ===")

from collections import Counter, defaultdict, namedtuple, deque

# Counter: 요소 개수 세기
text = "apple banana apple cherry banana apple"
counter = Counter(text.split())
print(f"Counter: {counter}")
print(f"가장 많은 2개: {counter.most_common(2)}")

# defaultdict: 기본값이 있는 딕셔너리
dd = defaultdict(list)
students = [("수학", "홍길동"), ("영어", "이영희"), ("수학", "김철수"), ("영어", "박지민")]
for subject, name in students:
    dd[subject].append(name)
print(f"defaultdict: {dict(dd)}")

# namedtuple: 이름 있는 튜플
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"namedtuple: {p}, x={p.x}, y={p.y}")

# deque: 양방향 큐
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(f"deque: {dq}")
dq.popleft()
print(f"popleft: {dq}")

print()


# ============================================================
# 7. itertools 모듈
# ============================================================
print("=== itertools 모듈 ===")

from itertools import product, combinations, permutations, chain

# product: 곱집합 (데카르트 곱)
colors = ["빨강", "파랑"]
sizes = ["S", "M", "L"]
combos = list(product(colors, sizes))
print(f"product: {combos}")

# combinations: 조합 (순서 무관, 중복 불가)
items = ["A", "B", "C", "D"]
combs = list(combinations(items, 2))
print(f"combinations: {combs}")

# permutations: 순열 (순서 중요)
perms = list(permutations(["A", "B", "C"], 2))
print(f"permutations: {perms}")

# chain: 여러 이터러블 연결
chained = list(chain([1, 2], [3, 4], [5, 6]))
print(f"chain: {chained}")

print()


# ============================================================
# 8. os & sys 모듈
# ============================================================
print("=== os & sys 모듈 ===")

import os
import sys

# os
print(f"현재 디렉토리: {os.getcwd()}")
print(f"플랫폼: {sys.platform}")
print(f"파이썬 버전: {sys.version}")

# os.path
filepath = "/Users/example/documents/report.pdf"
print(f"\n경로 분석:")
print(f"  디렉토리: {os.path.dirname(filepath)}")
print(f"  파일명: {os.path.basename(filepath)}")
print(f"  확장자: {os.path.splitext(filepath)[1]}")

print()


# ============================================================
# 9. pip으로 외부 패키지 설치
# ============================================================
print("=== pip 사용법 (참고) ===")

print("""
외부 패키지 설치 및 관리 명령어 (npm과 비교):

  pip install 패키지명           # npm install 패키지명
  pip install 패키지명==1.2.3    # npm install 패키지명@1.2.3
  pip uninstall 패키지명         # npm uninstall 패키지명
  pip list                       # npm list
  pip freeze > requirements.txt  # npm이 package.json에 자동 기록하는 것과 유사
  pip install -r requirements.txt  # npm install (package.json 기반 설치와 유사)

다음 Part 3에서 사용할 패키지:
  pip install pandas matplotlib scikit-learn
""")


# ============================================================
# 10. 실전 예제: 비밀번호 생성기
# ============================================================
print("=== 실전 예제: 비밀번호 생성기 ===")

import string

def generate_password(length=12, use_digits=True, use_special=True):
    """안전한 비밀번호를 생성"""
    characters = string.ascii_letters  # a-z, A-Z
    if use_digits:
        characters += string.digits     # 0-9
    if use_special:
        characters += string.punctuation  # !@#$...

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


for i in range(5):
    pw = generate_password(16)
    print(f"  비밀번호 {i+1}: {pw}")


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] random 모듈을 사용하여 로또 번호 생성기를 만드세요.
         (1~45에서 중복 없이 6개 선택, 정렬하여 출력)

[연습 2] datetime 모듈을 사용하여 자신의 생일부터 오늘까지
         며칠이 지났는지 계산하세요.

[연습 3] collections.Counter를 사용하여 문자열에서
         가장 많이 등장하는 문자 3개를 찾으세요.
"""

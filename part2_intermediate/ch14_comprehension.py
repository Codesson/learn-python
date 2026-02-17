"""
Chapter 14: 컴프리헨션 & 람다 (Comprehension & Lambda)
========================================================
파이썬스러운(Pythonic) 코드를 작성하는 핵심 기법을 배웁니다.
"""

# ============================================================
# JavaScript vs Python 비교 - 컴프리헨션 & 함수형
# ============================================================
#
#  JavaScript                                Python
#  ─────────────────────────────────────     ─────────────────────────────────
#  arr.map(x => x * 2)                      [x * 2 for x in arr]
#  arr.filter(x => x > 0)                   [x for x in arr if x > 0]
#  arr.map(x => x > 0 ? "양" : "음")        ["양" if x > 0 else "음" for x in arr]
#  arr.map(x => x * 2).filter(x => x > 5)   [x * 2 for x in arr if x * 2 > 5]
#
#  arr.map(fn)                               list(map(fn, arr))   또는 컴프리헨션
#  arr.filter(fn)                            list(filter(fn, arr)) 또는 컴프리헨션
#  arr.reduce(fn, init)                      functools.reduce(fn, arr, init)
#
#  (x) => x * 2                              lambda x: x * 2
#  arr.sort((a,b) => a - b)                  arr.sort()  (기본 오름차순)
#  arr.sort((a,b) => a.age - b.age)          arr.sort(key=lambda x: x["age"])
#
#  핵심 포인트:
#  Python의 리스트 컴프리헨션은 JS의 map + filter를 하나로 합친 것!
#  더 간결하고 가독성이 좋아서, Python에서는 map/filter보다 컴프리헨션을 선호합니다.
#

# ============================================================
# 1. 리스트 컴프리헨션 기초
# ============================================================
print("=== 리스트 컴프리헨션 기초 ===")

# 기존 방식
squares_old = []
for i in range(1, 6):
    squares_old.append(i ** 2)
print(f"기존 방식: {squares_old}")

# 리스트 컴프리헨션 (한 줄로!)
# JS: Array.from({length: 5}, (_, i) => (i+1) ** 2)
# JS: [1,2,3,4,5].map(i => i ** 2)
squares = [i ** 2 for i in range(1, 6)]
print(f"컴프리헨션: {squares}")

# 문법: [표현식 for 변수 in 반복가능객체]

# 더 많은 예제
evens = [i for i in range(1, 21) if i % 2 == 0]
print(f"1~20 짝수: {evens}")

words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]
print(f"대문자: {upper_words}")

lengths = [len(w) for w in words]
print(f"길이: {lengths}")

print()


# ============================================================
# 2. 조건부 컴프리헨션
# ============================================================
print("=== 조건부 컴프리헨션 ===")

# if 조건 (필터링)
# [표현식 for 변수 in 반복가능객체 if 조건]
nums = [1, -2, 3, -4, 5, -6, 7, -8]
positives = [n for n in nums if n > 0]
print(f"양수만: {positives}")

# if-else (변환)
# [참일때 if 조건 else 거짓일때 for 변수 in 반복가능객체]
labels = ["짝수" if n % 2 == 0 else "홀수" for n in range(1, 6)]
print(f"짝홀: {labels}")

# 절댓값 구하기
absolute = [n if n >= 0 else -n for n in nums]
print(f"절댓값: {absolute}")

print()


# ============================================================
# 3. 중첩 컴프리헨션
# ============================================================
print("=== 중첩 컴프리헨션 ===")

# 기존 방식: 구구단 쌍
pairs_old = []
for i in range(2, 5):
    for j in range(1, 4):
        pairs_old.append((i, j, i * j))

# 컴프리헨션
pairs = [(i, j, i * j) for i in range(2, 5) for j in range(1, 4)]
print("구구단 쌍:")
for a, b, c in pairs:
    print(f"  {a} × {b} = {c}")

# 2D 리스트(행렬) 생성
matrix = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
print(f"\n3×3 행렬: {matrix}")
for row in matrix:
    print(f"  {row}")

# 2D 리스트 평탄화 (flatten)
flat = [x for row in matrix for x in row]
print(f"평탄화: {flat}")

print()


# ============================================================
# 4. 딕셔너리 컴프리헨션
# ============================================================
print("=== 딕셔너리 컴프리헨션 ===")

# {키: 값 for 변수 in 반복가능객체}
squares_dict = {n: n ** 2 for n in range(1, 6)}
print(f"제곱: {squares_dict}")

# 두 리스트 합치기
names = ["홍길동", "이영희", "김철수"]
scores = [95, 88, 92]
score_dict = {name: score for name, score in zip(names, scores)}
print(f"점수: {score_dict}")

# 조건부
high_scores = {name: score for name, score in zip(names, scores) if score >= 90}
print(f"90점 이상: {high_scores}")

# 키-값 뒤집기
original = {"a": 1, "b": 2, "c": 3}
flipped = {v: k for k, v in original.items()}
print(f"뒤집기: {flipped}")

print()


# ============================================================
# 5. 셋 컴프리헨션
# ============================================================
print("=== 셋 컴프리헨션 ===")

# {표현식 for 변수 in 반복가능객체}
text = "Hello World Python Programming"
unique_lengths = {len(word) for word in text.split()}
print(f"고유한 단어 길이: {unique_lengths}")

# 중복 제거된 제곱수
nums = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {n ** 2 for n in nums}
print(f"고유 제곱수: {unique_squares}")

print()


# ============================================================
# 6. 제너레이터 표현식 (맛보기)
# ============================================================
print("=== 제너레이터 표현식 ===")

# 소괄호로 감싸면 제너레이터 (메모리 효율적)
gen = (i ** 2 for i in range(1, 6))
print(f"제너레이터: {gen}")
print(f"합계: {sum(gen)}")  # 55

# 큰 데이터에서 메모리 절약
# 리스트: 모든 값을 메모리에 저장
# 제너레이터: 값을 하나씩 생성 (lazy evaluation)
big_sum = sum(i for i in range(1, 1000001))
print(f"1~1000000 합: {big_sum}")

print()


# ============================================================
# 7. lambda 함수
# ============================================================
print("=== lambda 함수 ===")

# lambda 매개변수: 표현식
# 이름 없는 한 줄짜리 함수

# 기본 사용
square = lambda x: x ** 2
add = lambda a, b: a + b

print(f"square(5) = {square(5)}")
print(f"add(3, 4) = {add(3, 4)}")

# 일반 함수와 비교
def square_func(x):
    return x ** 2

# 둘은 동일한 기능!

print()


# ============================================================
# 8. map() - 변환
# ============================================================
print("=== map() ===")

# map(함수, 반복가능객체): 각 요소에 함수를 적용
# JS: numbers.map(x => x ** 2)
# Python: list(map(lambda x: x ** 2, numbers))  또는  [x**2 for x in numbers]
numbers = [1, 2, 3, 4, 5]

# lambda와 함께
squares = list(map(lambda x: x ** 2, numbers))
print(f"제곱: {squares}")

# 문자열을 정수로 변환
str_nums = ["10", "20", "30", "40"]
int_nums = list(map(int, str_nums))
print(f"변환: {int_nums}")

# 리스트 컴프리헨션과 비교 (둘 다 동일한 결과)
squares_comp = [x ** 2 for x in numbers]
print(f"컴프리헨션: {squares_comp}")

print()


# ============================================================
# 9. filter() - 필터링
# ============================================================
print("=== filter() ===")

# filter(함수, 반복가능객체): 조건이 True인 요소만 남김
# JS: numbers.filter(x => x > 0)
# Python: list(filter(lambda x: x > 0, numbers))  또는  [x for x in numbers if x > 0]
numbers = [1, -2, 3, -4, 5, -6, 7, -8]

# 양수만
positives = list(filter(lambda x: x > 0, numbers))
print(f"양수: {positives}")

# 짝수만
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"짝수: {evens}")

# 빈 문자열 제거
words = ["hello", "", "world", "", "python", ""]
non_empty = list(filter(None, words))  # None은 falsy 값 제거
print(f"비어있지 않은: {non_empty}")

print()


# ============================================================
# 10. sorted()와 lambda
# ============================================================
print("=== sorted() + lambda ===")

# 학생 데이터
students = [
    {"name": "홍길동", "age": 25, "score": 85},
    {"name": "이영희", "age": 22, "score": 95},
    {"name": "김철수", "age": 28, "score": 78},
    {"name": "박지민", "age": 20, "score": 92},
]

# 점수 순 정렬
# JS: students.sort((a, b) => b.score - a.score)
# Python은 key 함수로 비교 기준을 지정! (비교 함수 대신 키 추출)
by_score = sorted(students, key=lambda s: s["score"], reverse=True)
print("점수 내림차순:")
for s in by_score:
    print(f"  {s['name']}: {s['score']}점")

# 나이 순 정렬
by_age = sorted(students, key=lambda s: s["age"])
print("\n나이 오름차순:")
for s in by_age:
    print(f"  {s['name']}: {s['age']}세")

# 여러 기준 정렬
data = [(2, "b"), (1, "a"), (2, "a"), (1, "b")]
sorted_data = sorted(data, key=lambda x: (x[0], x[1]))
print(f"\n다중 기준 정렬: {sorted_data}")

print()


# ============================================================
# 11. reduce() - 누적 연산
# ============================================================
print("=== reduce() ===")
from functools import reduce

# reduce(함수, 반복가능객체): 누적 연산
# JS: numbers.reduce((a, b) => a + b, 0)  ← 배열 메서드
# Python: reduce(lambda a, b: a + b, numbers)  ← 별도 import 필요
numbers = [1, 2, 3, 4, 5]

# 합계
total = reduce(lambda a, b: a + b, numbers)
print(f"합계: {total}")          # 15

# 곱
product = reduce(lambda a, b: a * b, numbers)
print(f"곱: {product}")          # 120

# 최대값
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(f"최대: {maximum}")        # 5


# ============================================================
# 12. 실전 예제: 데이터 파이프라인
# ============================================================
print("\n=== 실전 예제: 데이터 처리 ===")

# 원본 데이터
raw_data = [
    "  Alice,85  ",
    "  Bob,92  ",
    "  Charlie,  ",
    "  Diana,78  ",
    "  Eve,95  ",
    "  Frank,  ",
]

# 1) 공백 제거
cleaned = [s.strip() for s in raw_data]

# 2) 이름과 점수 분리
parsed = [s.split(",") for s in cleaned]

# 3) 점수가 있는 것만 필터링
valid = [(name, int(score)) for name, score in parsed if score.strip()]

# 4) 점수 내림차순 정렬
ranked = sorted(valid, key=lambda x: x[1], reverse=True)

print("성적 순위:")
for i, (name, score) in enumerate(ranked, 1):
    print(f"  {i}위: {name} - {score}점")

# 평균
avg = sum(score for _, score in valid) / len(valid)
print(f"평균: {avg:.1f}점")


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] 1~100에서 3의 배수이면서 5의 배수가 아닌 수의 리스트를
         컴프리헨션으로 만드세요.

[연습 2] 문장에서 각 단어의 글자 수를 딕셔너리 컴프리헨션으로 만드세요.
         "Python is a great programming language"
         → {"Python": 6, "is": 2, "a": 1, ...}

[연습 3] 리스트의 모든 요소를 문자열로 변환하여 쉼표로 연결하는
         한 줄 코드를 작성하세요.
         [1, 2, 3, 4, 5] → "1, 2, 3, 4, 5"

[연습 4] map과 filter를 조합하여, 문자열 리스트에서 길이가 3 이상인
         문자열만 대문자로 변환하세요.
"""

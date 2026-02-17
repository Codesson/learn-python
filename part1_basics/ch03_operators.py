"""
Chapter 03: 연산자 (Operators)
================================
파이썬의 다양한 연산자를 배웁니다.
"""

# ============================================================
# JavaScript vs Python 비교 - 연산자
# ============================================================
#
#  JavaScript                      Python
#  ─────────────────────────────    ─────────────────────────────
#  Math.floor(a / b)               a // b          (정수 나누기가 연산자로 존재!)
#  a ** b                          a ** b          (동일!)
#  a % b                           a % b           (동일, 단 음수 처리 다름)
#
#  === (엄격 비교)                 == (Python의 ==은 이미 엄격!)
#  == (느슨 비교)                  (없음 - Python에 느슨 비교 없음!)
#  !== (엄격 불일치)               !=
#
#  && || !                         and  or  not    (기호 대신 영어 키워드!)
#  a ? b : c (삼항)                b if a else c   (순서가 다름!)
#
#  typeof x                        type(x)
#  x instanceof Array              isinstance(x, list)
#  'key' in obj                    'key' in dict   (동일 개념!)
#  arr.includes(val)               val in list     (순서 반대!)
#

# ============================================================
# 1. 산술 연산자
# ============================================================
print("=== 산술 연산자 ===")

a, b = 10, 3

print(f"{a} + {b} = {a + b}")      # 더하기: 13
print(f"{a} - {b} = {a - b}")      # 빼기: 7
print(f"{a} * {b} = {a * b}")      # 곱하기: 30
print(f"{a} / {b} = {a / b}")      # 나누기: 3.3333... (항상 float 반환)
print(f"{a} // {b} = {a // b}")    # 몫 (정수 나누기): 3  ← JS에는 없음! Math.floor(a/b)
print(f"{a} % {b} = {a % b}")      # 나머지: 1
print(f"{a} ** {b} = {a ** b}")    # 거듭제곱: 1000  (JS와 동일!)

# 나누기 vs 정수 나누기
print(f"\n7 / 2 = {7 / 2}")        # 3.5 (float)
print(f"7 // 2 = {7 // 2}")        # 3 (int)
print(f"-7 // 2 = {-7 // 2}")      # -4 (음수일 때 주의: 내림)

print()


# ============================================================
# 2. 비교 연산자
# ============================================================
print("=== 비교 연산자 ===")

x, y = 5, 10

# Python의 ==는 JS의 ===와 같은 엄격 비교입니다!
# Python에는 JS의 == (느슨 비교, 타입 변환 비교)가 없습니다.
# 즉, "3" == 3 → JS: true (느슨), Python: False (항상 엄격)
print(f"{x} == {y} : {x == y}")    # 같다: False     (JS의 ===에 해당)
print(f"{x} != {y} : {x != y}")    # 다르다: True    (JS의 !==에 해당)
print(f"{x} > {y}  : {x > y}")     # 크다: False
print(f"{x} < {y}  : {x < y}")     # 작다: True
print(f"{x} >= {y} : {x >= y}")    # 크거나 같다: False
print(f"{x} <= {y} : {x <= y}")    # 작거나 같다: True

# 연쇄 비교 (파이썬의 강력한 기능!)
age = 25
print(f"\n18 <= {age} < 30 : {18 <= age < 30}")   # True
print(f"1 < 2 < 3 : {1 < 2 < 3}")                 # True
print(f"1 < 2 > 0 : {1 < 2 > 0}")                 # True

print()


# ============================================================
# 3. 논리 연산자
# ============================================================
print("=== 논리 연산자 ===")

# JS: &&, ||, !  →  Python: and, or, not  (기호 대신 영어 키워드!)
# and: 둘 다 True일 때만 True
print(f"True and True   = {True and True}")      # True
print(f"True and False  = {True and False}")      # False

# or: 하나라도 True이면 True
print(f"False or True   = {False or True}")       # True
print(f"False or False  = {False or False}")      # False

# not: 반대로 뒤집기
print(f"not True        = {not True}")            # False
print(f"not False       = {not False}")           # True

# 실전 예시: 나이와 학생 여부로 할인 판단
age = 22
is_student = True
gets_discount = age < 25 and is_student
print(f"\n나이: {age}, 학생: {is_student}")
print(f"할인 대상: {gets_discount}")               # True

# 단축 평가 (Short-circuit Evaluation)
# JS의 &&, ||과 완전히 동일한 동작!
# and: 첫 번째가 False이면 두 번째는 평가하지 않음
# or: 첫 번째가 True이면 두 번째는 평가하지 않음
print(f"\n0 and 'hello' = {0 and 'hello'}")        # 0 (첫 값이 falsy)
print(f"1 and 'hello' = {1 and 'hello'}")          # 'hello' (첫 값이 truthy → 두 번째 반환)
print(f"0 or 'hello'  = {0 or 'hello'}")           # 'hello' (첫 값이 falsy → 두 번째 반환)
print(f"1 or 'hello'  = {1 or 'hello'}")           # 1 (첫 값이 truthy)

# 실전 활용: 기본값 설정 (JS의 || 기본값 패턴과 동일!)
# JS: const displayName = username || "익명"
username = ""
display_name = username or "익명"
print(f"표시 이름: {display_name}")                 # "익명"
# 참고: JS의 ?? (nullish coalescing)은 Python에 없음. or로 대체합니다.

print()


# ============================================================
# 4. 할당 연산자
# ============================================================
print("=== 할당 연산자 ===")

# JS에서는 n++, n-- 가 있지만, Python에는 없습니다!
# n++ 대신 n += 1을 사용합니다.
n = 10
print(f"n = {n}")

n += 5    # n = n + 5
print(f"n += 5  → {n}")    # 15

n -= 3    # n = n - 3
print(f"n -= 3  → {n}")    # 12

n *= 2    # n = n * 2
print(f"n *= 2  → {n}")    # 24

n /= 4    # n = n / 4
print(f"n /= 4  → {n}")    # 6.0

n //= 2   # n = n // 2
print(f"n //= 2 → {n}")    # 3.0

n **= 3   # n = n ** 3
print(f"n **= 3 → {n}")    # 27.0

n %= 5    # n = n % 5
print(f"n %= 5  → {n}")    # 2.0

print()


# ============================================================
# 5. 멤버십 연산자 (in, not in)
# ============================================================
print("=== 멤버십 연산자 ===")

# JS: fruits.includes("사과")  →  Python: "사과" in fruits  (더 직관적!)
fruits = ["사과", "바나나", "딸기"]
print(f"'사과' in {fruits}: {'사과' in fruits}")           # True
print(f"'포도' in {fruits}: {'포도' in fruits}")           # False
print(f"'포도' not in {fruits}: {'포도' not in fruits}")   # True

# 문자열에서도 사용 가능
message = "Hello, Python!"
print(f"'Python' in '{message}': {'Python' in message}")  # True

print()


# ============================================================
# 6. 항등 연산자 (is, is not)
# ============================================================
print("=== 항등 연산자 ===")

# is: 같은 객체인지(참조 동일) 확인 (메모리 주소 비교)
# ==: 값이 같은지 확인
# JS와 비교: Python의 is는 JS의 === (객체 참조 비교)와 유사
#            Python의 ==는 JS의 깊은 비교(deep equality)와 유사

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b : {a == b}")    # True (값이 같음)
print(f"a is b : {a is b}")    # False (다른 객체)
print(f"a is c : {a is c}")    # True (같은 객체)

# None 비교는 항상 is를 사용
value = None
print(f"value is None : {value is None}")    # True


# ============================================================
# 7. 연산자 우선순위 (높은 순서)
# ============================================================
print("\n=== 연산자 우선순위 ===")
# 1. ** (거듭제곱)
# 2. +x, -x (단항 연산)
# 3. *, /, //, %
# 4. +, -
# 5. ==, !=, <, >, <=, >=, is, in
# 6. not
# 7. and
# 8. or

# 예시
result = 2 + 3 * 4          # 14 (곱셈 먼저)
print(f"2 + 3 * 4 = {result}")

result = (2 + 3) * 4        # 20 (괄호 먼저)
print(f"(2 + 3) * 4 = {result}")

result = 2 ** 3 ** 2        # 512 (거듭제곱은 오른쪽부터: 2^(3^2) = 2^9)
print(f"2 ** 3 ** 2 = {result}")


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] 섭씨 온도를 입력받아 화씨로 변환하세요.
         공식: 화씨 = 섭씨 * 9/5 + 32

[연습 2] 정수를 입력받아 짝수인지 홀수인지 판별하세요.
         (힌트: % 연산자 사용)

[연습 3] 다음 식의 결과를 예측한 후 확인하세요.
         True and not False or False
         3 > 2 and 2 > 1
         not (3 > 2 and 2 > 1)
"""

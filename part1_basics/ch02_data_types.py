"""
Chapter 02: 자료형 (Data Types)
================================
파이썬의 기본 자료형과 형변환을 배웁니다.
"""

# ============================================================
# JavaScript vs Python 비교 - 자료형
# ============================================================
#
#  JavaScript                      Python
#  ─────────────────────────────    ─────────────────────────────
#  number (정수/실수 구분 없음)     int (정수) + float (실수) 별도!
#  string                          str
#  boolean (true/false)            bool (True/False) ← 대문자 주의!
#  null                            None
#  undefined                       (없음)
#  BigInt (123n)                   int (기본적으로 크기 무제한!)
#  NaN                             float('nan')
#  Infinity                        float('inf') 또는 math.inf
#
#  Number("42")                    int("42")
#  String(42)                      str(42)
#  Boolean(0) → false              bool(0) → False
#  parseInt("3.14")                int("3.14") → 에러! int(float("3.14"))
#  parseFloat("3.14")              float("3.14")
#

# ============================================================
# 1. 숫자형 - 정수 (int)
# ============================================================
a = 10
b = -3
c = 0

print("=== 정수(int) ===")
print(a, type(a))
print(b, type(b))

# 큰 숫자도 자유롭게 사용 가능 (파이썬은 정수 크기 제한이 없음)
# JS에서는 BigInt(999999999999999999999n)가 필요하지만, Python은 기본 int로 가능!
big_number = 999999999999999999999
print("큰 숫자:", big_number)

# 다른 진법 표현
binary = 0b1010     # 2진수 (10)
octal = 0o17        # 8진수 (15)
hexa = 0xFF         # 16진수 (255)
print(f"2진수 0b1010 = {binary}")
print(f"8진수 0o17 = {octal}")
print(f"16진수 0xFF = {hexa}")

print()


# ============================================================
# 2. 숫자형 - 실수 (float)
# ============================================================
pi = 3.14159
temperature = -12.5

print("=== 실수(float) ===")
print(pi, type(pi))
print(temperature, type(temperature))

# 지수 표기법
scientific = 1.5e3   # 1.5 × 10^3 = 1500.0
tiny = 2.5e-4        # 2.5 × 10^-4 = 0.00025
print(f"1.5e3 = {scientific}")
print(f"2.5e-4 = {tiny}")

# 주의: 부동소수점 오차 (JS와 동일한 문제!)
# JS에서도 0.1 + 0.2 === 0.30000000000000004 였죠? 같은 IEEE 754 표준
print(0.1 + 0.2)            # 0.30000000000000004 (정확히 0.3이 아님!)
print(0.1 + 0.2 == 0.3)     # False

print()


# ============================================================
# 3. 문자열 (str)
# ============================================================
str1 = "큰따옴표 문자열"
str2 = '작은따옴표 문자열'
str3 = """여러 줄
문자열도
가능합니다."""

print("=== 문자열(str) ===")
print(str1)
print(str2)
print(str3)
print(type(str1))

# 이스케이프 문자
print("줄바꿈:\n여기서 새 줄")
print("탭:\t여기서 탭")
print("따옴표: \"큰따옴표\" \'작은따옴표\'")
print("백슬래시: \\")

print()


# ============================================================
# 4. 불리언 (bool)
# ============================================================
# 핵심 차이: JS는 true/false (소문자), Python은 True/False (대문자!)
is_true = True       # JS: true
is_false = False     # JS: false

print("=== 불리언(bool) ===")
print(is_true, type(is_true))
print(is_false, type(is_false))

# bool은 int의 하위 클래스 (True=1, False=0)
print("True + True =", True + True)     # 2
print("True * 10 =", True * 10)         # 10
print("False + 1 =", False + 1)         # 1

# 다양한 값의 참/거짓 (Truthy / Falsy)
# JS와 거의 동일한 개념! 하지만 차이점에 주의:
# - JS falsy: 0, "", null, undefined, NaN, false
# - Python falsy: 0, "", None, False, [], {}, (), set()  ← 빈 컬렉션도 falsy!
print("\n--- Truthy / Falsy ---")
print(bool(1))       # True  (0이 아닌 숫자)
print(bool(0))       # False (0)
print(bool("hello")) # True  (비어있지 않은 문자열)
print(bool(""))      # False (빈 문자열)
print(bool([1, 2]))  # True  (비어있지 않은 리스트)
print(bool([]))      # False (빈 리스트)
print(bool(None))    # False (None)

print()


# ============================================================
# 5. None 타입
# ============================================================
# None은 "값이 없음"을 나타내는 특별한 값입니다.
# JS의 null과 유사합니다. 단, Python에는 undefined가 없습니다!
# 정의되지 않은 변수에 접근하면 undefined가 아니라 NameError가 발생합니다.
nothing = None
print("=== None ===")
print(nothing, type(nothing))
print(nothing is None)    # True (None 비교는 is를 사용, JS의 === null과 유사)

print()


# ============================================================
# 6. 형변환 (Type Conversion)
# ============================================================
print("=== 형변환 ===")

# int() - 정수로 변환
print(int(3.7))       # 3     (소수점 버림)
print(int("42"))      # 42    (문자열 → 정수)
print(int(True))      # 1     (bool → 정수)

# float() - 실수로 변환
print(float(10))      # 10.0
print(float("3.14"))  # 3.14

# str() - 문자열로 변환
print(str(100))       # "100"
print(str(3.14))      # "3.14"
print(str(True))      # "True"

# bool() - 불리언으로 변환
print(bool(0))        # False
print(bool(42))       # True
print(bool(""))       # False
print(bool("hello"))  # True

# 형변환 에러 예시 (주석 해제하면 에러 발생)
# int("hello")        # ValueError: 문자열을 정수로 변환 불가
# int("3.14")         # ValueError: 소수점 문자열은 바로 int 변환 불가

# 올바른 방법: 소수점 문자열 → float → int
print(int(float("3.14")))   # 3

print()


# ============================================================
# 7. id() - 객체의 메모리 주소 확인
# ============================================================
x = 10
y = 10
z = 20

print("=== id() 메모리 주소 ===")
print(f"x의 id: {id(x)}")
print(f"y의 id: {id(y)}")
print(f"z의 id: {id(z)}")
print(f"x와 y는 같은 객체? {x is y}")  # True (작은 정수는 캐싱됨)


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] 다음 값들의 타입을 예측한 뒤, type()으로 확인해 보세요.
         42, 42.0, "42", True, None, [1, 2, 3]

[연습 2] 사용자에게 두 개의 숫자를 입력받아 합계를 출력하세요.
         (힌트: input()은 문자열을 반환하므로 형변환이 필요합니다)

[연습 3] 아래 형변환의 결과를 예측해 보세요.
         int(7.9)
         float(3)
         str(False)
         bool(-1)
         bool(0.0)
"""

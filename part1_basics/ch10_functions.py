"""
Chapter 10: 함수 (Functions)
==============================
재사용 가능한 코드 블록인 함수를 배웁니다.
"""

# ============================================================
# JavaScript vs Python 비교 - 함수
# ============================================================
#
#  JavaScript                           Python
#  ─────────────────────────────────    ─────────────────────────────
#  function greet() {}                  def greet():
#  const greet = () => {}              def greet():  (화살표 함수 없음)
#  (x) => x * 2                        lambda x: x * 2
#  function(a, b=10) {}                def func(a, b=10):    (동일!)
#  function(...args) {}                def func(*args):      (...rest → *args)
#  function({name, age}) {}            (구조분해 매개변수 없음)
#
#  return 값                            return 값              (동일!)
#  return {a, b}                        return a, b            (튜플로 반환!)
#  const [a, b] = func()               a, b = func()          (언패킹!)
#
#  호이스팅 있음                        호이스팅 없음 (정의 후 호출!)
#  클로저 있음                          클로저 있음            (동일!)
#  this 바인딩                          self 명시적 전달 (메서드에서)
#
#  핵심 차이:
#  1) def 키워드로 정의 (function → def)
#  2) 화살표 함수(=>) 없음, lambda로 한 줄 함수만 가능
#  3) ...rest → *args, 구조분해 → **kwargs
#  4) 여러 값 반환이 간단 (return a, b → 튜플)
#

# ============================================================
# 1. 함수 정의와 호출
# ============================================================
print("=== 함수 기초 ===")


def greet():       # JS: function greet() { ... }
    """인사말을 출력하는 함수"""
    print("안녕하세요!")
    print("파이썬 학습에 오신 것을 환영합니다!")


# 함수 호출
greet()
greet()  # 원하는 만큼 재사용

print()


# ============================================================
# 2. 매개변수와 인자
# ============================================================
print("=== 매개변수 ===")


def greet_person(name):
    """이름을 받아 인사하는 함수"""
    print(f"안녕하세요, {name}님!")


greet_person("홍길동")
greet_person("이영희")

print()


# 여러 개의 매개변수
def add(a, b):
    """두 수의 합을 출력"""
    print(f"{a} + {b} = {a + b}")


add(3, 5)
add(10, 20)

print()


# ============================================================
# 3. return - 값 반환
# ============================================================
print("=== return ===")


def multiply(a, b):
    """두 수의 곱을 반환"""
    return a * b


result = multiply(4, 5)
print(f"4 × 5 = {result}")

# return이 없으면 None을 반환
def say_hello():
    print("Hello!")

return_value = say_hello()
print(f"반환값: {return_value}")  # None


# 여러 값 반환 (튜플로)
# JS에서는 return { min, max, avg } 또는 return [min, max, avg] 해야 하지만
# Python은 그냥 return a, b, c 로 간단하게 여러 값 반환!
def get_stats(numbers):
    """리스트의 통계를 반환"""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


minimum, maximum, average = get_stats([85, 92, 78, 95, 88])
print(f"\n최소: {minimum}, 최대: {maximum}, 평균: {average}")

print()


# ============================================================
# 4. 기본값 매개변수
# ============================================================
print("=== 기본값 매개변수 ===")


def power(base, exponent=2):
    """거듭제곱 계산 (기본값: 제곱)"""
    return base ** exponent


print(f"power(3)    = {power(3)}")       # 9 (3^2)
print(f"power(3, 3) = {power(3, 3)}")    # 27 (3^3)
print(f"power(2, 10) = {power(2, 10)}")  # 1024 (2^10)


def create_profile(name, age, city="서울", job="학생"):
    """프로필 생성"""
    return {"name": name, "age": age, "city": city, "job": job}


profile1 = create_profile("홍길동", 25)
profile2 = create_profile("이영희", 30, "부산", "개발자")
print(f"\n{profile1}")
print(f"{profile2}")

print()


# ============================================================
# 5. 키워드 인자
# ============================================================
print("=== 키워드 인자 ===")


def describe_pet(name, animal_type, age):
    """반려동물 정보 출력"""
    print(f"이름: {name}, 종류: {animal_type}, 나이: {age}살")


# 위치 인자
describe_pet("멍멍이", "강아지", 3)

# 키워드 인자 (순서 상관없음)
describe_pet(age=2, name="야옹이", animal_type="고양이")

# 혼합 (위치 인자가 먼저!)
describe_pet("짹짹이", animal_type="앵무새", age=1)

print()


# ============================================================
# 6. *args - 가변 위치 인자
# ============================================================
print("=== *args ===")


def sum_all(*numbers):    # JS: function sumAll(...numbers) { }
    """여러 숫자의 합을 반환"""
    # *args는 JS의 ...rest 파라미터와 동일한 개념!
    # 차이: JS에서는 배열(Array), Python에서는 튜플(tuple)로 받음
    print(f"  받은 인자: {numbers} (type: {type(numbers)})")
    return sum(numbers)


print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20, 30, 40, 50) = {sum_all(10, 20, 30, 40, 50)}")

print()


# ============================================================
# 7. **kwargs - 가변 키워드 인자
# ============================================================
print("=== **kwargs ===")


def print_info(**kwargs):     # JS에는 직접적인 대응이 없음
    """키워드 인자들을 출력"""
    # **kwargs는 이름 붙은 인자들을 딕셔너리로 받습니다.
    # JS에서 구조분해: function({name, age, ...rest}) 와 유사한 개념
    print(f"  받은 인자: {kwargs} (type: {type(kwargs)})")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


print_info(name="홍길동", age=25, city="서울")

print()


# *args와 **kwargs를 함께 사용
def flexible(required, *args, **kwargs):
    """다양한 형태의 인자를 받는 함수"""
    print(f"  필수: {required}")
    print(f"  추가 위치 인자: {args}")
    print(f"  추가 키워드 인자: {kwargs}")


flexible("첫번째", 2, 3, 4, name="홍길동", age=25)

print()


# ============================================================
# 8. 변수의 스코프 (Scope)
# ============================================================
print("=== 변수 스코프 ===")

# JS와 스코프 차이:
# - JS: var(함수 스코프), let/const(블록 스코프)
# - Python: 함수 스코프만! (if/for 블록은 스코프를 만들지 않음!)
#   즉, for 루프 안에서 선언한 변수도 루프 밖에서 접근 가능!
global_var = "전역 변수"


def scope_test():
    local_var = "지역 변수"
    print(f"  함수 내부 - global_var: {global_var}")
    print(f"  함수 내부 - local_var: {local_var}")


scope_test()
print(f"함수 외부 - global_var: {global_var}")
# print(local_var)  # NameError! 함수 밖에서 접근 불가


# global 키워드
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
increment()
print(f"\ncounter = {counter}")   # 3

print()


# ============================================================
# 9. 람다 함수 (맛보기 - ch14에서 자세히)
# ============================================================
print("=== 람다 함수 ===")

# 한 줄짜리 간단한 함수
# JS의 화살표 함수와 유사하지만, 단일 표현식만 가능!
# JS: const square = (x) => x ** 2
# Python: square = lambda x: x ** 2
square = lambda x: x ** 2
add = lambda a, b: a + b

print(f"square(5) = {square(5)}")
print(f"add(3, 4) = {add(3, 4)}")

# 정렬에서 활용
students = [("홍길동", 85), ("이영희", 92), ("김철수", 78)]
students.sort(key=lambda x: x[1], reverse=True)
print(f"점수 내림차순: {students}")

print()


# ============================================================
# 10. 재귀 함수 (Recursion)
# ============================================================
print("=== 재귀 함수 ===")


def factorial(n):
    """팩토리얼을 재귀로 계산"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(f"5! = {factorial(5)}")     # 120
print(f"10! = {factorial(10)}")   # 3628800


def fibonacci(n):
    """피보나치 수열의 n번째 값"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(f"\n피보나치 수열 (처음 10개):")
for i in range(10):
    print(fibonacci(i), end=" ")
print()

print()


# ============================================================
# 11. 함수 독스트링과 타입 힌트
# ============================================================
print("=== 타입 힌트 & 독스트링 ===")


def calculate_bmi(weight: float, height: float) -> float:
    """
    BMI(체질량지수)를 계산합니다.

    Args:
        weight: 체중 (kg)
        height: 키 (m)

    Returns:
        BMI 값
    """
    return weight / (height ** 2)


bmi = calculate_bmi(70, 1.75)
print(f"BMI: {bmi:.1f}")
print(f"함수 설명: {calculate_bmi.__doc__}")


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] 섭씨를 화씨로 변환하는 함수와,
         화씨를 섭씨로 변환하는 함수를 각각 작성하세요.

[연습 2] 리스트를 받아 짝수만 필터링하여 반환하는 함수를 작성하세요.
         예: filter_even([1,2,3,4,5,6]) → [2, 4, 6]

[연습 3] 가변 인자를 받아 평균을 계산하는 함수를 작성하세요.
         예: average(10, 20, 30) → 20.0

[연습 4] 재귀 함수를 사용하여 거듭제곱을 계산하세요.
         예: my_power(2, 10) → 1024
"""

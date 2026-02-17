"""
Chapter 04: 문자열 다루기 (Strings)
====================================
문자열의 인덱싱, 슬라이싱, 다양한 메서드를 배웁니다.
"""

# ============================================================
# JavaScript vs Python 비교 - 문자열
# ============================================================
#
#  JavaScript                      Python
#  ─────────────────────────────    ─────────────────────────────
#  `Hello ${name}`                 f"Hello {name}"    (f-string)
#  str[0]                          str[0]             (동일!)
#  str.slice(1, 3)                 str[1:3]           (슬라이싱!)
#  str.length                      len(str)           (속성 → 함수)
#  str.toUpperCase()               str.upper()
#  str.toLowerCase()               str.lower()
#  str.trim()                      str.strip()
#  str.includes("abc")             "abc" in str       (in 연산자!)
#  str.indexOf("abc")              str.find("abc")    (-1 반환 동일)
#  str.replace("a", "b")           str.replace("a", "b")  (동일!)
#  str.split(",")                  str.split(",")          (동일!)
#  arr.join("-")                   "-".join(arr)      (순서 반대!)
#  str.startsWith("abc")           str.startswith("abc")  (camelCase → snake_case)
#  str.endsWith("abc")             str.endswith("abc")
#  str.repeat(3)                   str * 3            (* 연산자!)
#  str.padStart(10, "0")           str.zfill(10) 또는 str.rjust(10, "0")
#
#  참고: Python 문자열도 JS처럼 불변(immutable)입니다!
#

# ============================================================
# 1. 문자열 인덱싱 (Indexing)
# ============================================================
print("=== 인덱싱 ===")

text = "Python"
#       P  y  t  h  o  n
# 양수: 0  1  2  3  4  5
# 음수:-6 -5 -4 -3 -2 -1

print(f"text = '{text}'")
print(f"text[0] = '{text[0]}'")     # P (첫 번째 글자)
print(f"text[1] = '{text[1]}'")     # y
print(f"text[-1] = '{text[-1]}'")   # n (마지막 글자)
print(f"text[-2] = '{text[-2]}'")   # o

print()


# ============================================================
# 2. 문자열 슬라이싱 (Slicing)
# ============================================================
print("=== 슬라이싱 ===")
# text[시작:끝:간격]  → 시작 이상, 끝 미만
# JS의 slice()와 비슷하지만, 간격(step)까지 지정 가능!
# JS: text.slice(0, 5)  →  Python: text[0:5]

text = "Hello, Python!"

print(f"text[0:5]   = '{text[0:5]}'")     # Hello
print(f"text[7:]    = '{text[7:]}'")       # Python!
print(f"text[:5]    = '{text[:5]}'")       # Hello
print(f"text[-7:]   = '{text[-7:]}'")      # Python!
print(f"text[::2]   = '{text[::2]}'")      # Hlo yhn (2칸씩 건너뛰기)
print(f"text[::-1]  = '{text[::-1]}'")     # !nohtyP ,olleH (뒤집기)

print()


# ============================================================
# 3. 문자열 연산
# ============================================================
print("=== 문자열 연산 ===")

# 연결 (+)
first = "Hello"
second = "World"
greeting = first + ", " + second + "!"
print(greeting)            # Hello, World!

# 반복 (*)
line = "-" * 30
print(line)                # ------------------------------

# 길이 (len)
msg = "파이썬 공부"
print(f"'{msg}'의 길이: {len(msg)}")   # 6 (공백 포함)

print()


# ============================================================
# 4. 문자열 포매팅 (Formatting)
# ============================================================
print("=== 문자열 포매팅 ===")

name = "홍길동"
age = 25
score = 95.678

# 방법 1: f-string (추천! 파이썬 3.6+)
# JS의 템플릿 리터럴과 매우 유사!
# JS: `이름: ${name}, 나이: ${age}`
# Python: f"이름: {name}, 나이: {age}"
# 차이: 백틱(`) 대신 f"", ${} 대신 {}
print(f"이름: {name}, 나이: {age}")
print(f"점수: {score:.2f}")              # 소수점 2자리
print(f"{'제목':^20}")                    # 20칸 가운데 정렬
print(f"{'왼쪽':<20}")                    # 20칸 왼쪽 정렬
print(f"{'오른쪽':>20}")                  # 20칸 오른쪽 정렬
print(f"{'채우기':*^20}")                 # *로 채우면서 가운데 정렬
print(f"큰 숫자: {1234567:,}")            # 천 단위 콤마

# 방법 2: format() 메서드
print("이름: {}, 나이: {}".format(name, age))
print("이름: {n}, 나이: {a}".format(n=name, a=age))

# 방법 3: % 포매팅 (오래된 방식)
print("이름: %s, 나이: %d" % (name, age))

print()


# ============================================================
# 5. 문자열 메서드 - 대소문자
# ============================================================
print("=== 대소문자 메서드 ===")

s = "hello, Python World!"

print(f"upper()      : {s.upper()}")        # 전부 대문자
print(f"lower()      : {s.lower()}")        # 전부 소문자
print(f"capitalize() : {s.capitalize()}")   # 첫 글자만 대문자
print(f"title()      : {s.title()}")        # 각 단어 첫 글자 대문자
print(f"swapcase()   : {s.swapcase()}")     # 대소문자 반전

print()


# ============================================================
# 6. 문자열 메서드 - 검색
# ============================================================
print("=== 검색 메서드 ===")

s = "Hello, Python! Python is great!"

print(f"find('Python')    : {s.find('Python')}")         # 7 (첫 번째 위치)
print(f"find('Java')      : {s.find('Java')}")           # -1 (없으면 -1)
print(f"rfind('Python')   : {s.rfind('Python')}")        # 15 (마지막 위치)
print(f"count('Python')   : {s.count('Python')}")        # 2 (등장 횟수)
print(f"startswith('Hello'): {s.startswith('Hello')}")    # True
print(f"endswith('!')      : {s.endswith('!')}")          # True
print(f"'Python' in s      : {'Python' in s}")           # True

print()


# ============================================================
# 7. 문자열 메서드 - 변환
# ============================================================
print("=== 변환 메서드 ===")

s = "  Hello, Python!  "

print(f"strip()   : '{s.strip()}'")       # 양쪽 공백 제거
print(f"lstrip()  : '{s.lstrip()}'")      # 왼쪽 공백 제거
print(f"rstrip()  : '{s.rstrip()}'")      # 오른쪽 공백 제거

s2 = "Hello, World!"
print(f"replace() : {s2.replace('World', 'Python')}")   # 치환

print()


# ============================================================
# 8. 문자열 메서드 - 분리 & 결합
# ============================================================
print("=== 분리 & 결합 ===")

# split(): 문자열 → 리스트
csv_data = "사과,바나나,딸기,포도"
fruits = csv_data.split(",")
print(f"split(',') : {fruits}")     # ['사과', '바나나', '딸기', '포도']

sentence = "파이썬 학습은 재미있다"
words = sentence.split()            # 공백 기준 분리 (기본)
print(f"split()    : {words}")

# join(): 리스트 → 문자열
# 주의! JS와 순서가 반대입니다!
# JS: fruits.join(" - ")  →  Python: " - ".join(fruits)
result = " - ".join(fruits)
print(f"join()     : {result}")     # 사과 - 바나나 - 딸기 - 포도

print()


# ============================================================
# 9. 문자열 메서드 - 판별
# ============================================================
print("=== 판별 메서드 ===")

print(f"'abc'.isalpha()   : {'abc'.isalpha()}")       # True (문자만)
print(f"'123'.isdigit()   : {'123'.isdigit()}")       # True (숫자만)
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")    # True (문자+숫자)
print(f"'   '.isspace()   : {'   '.isspace()}")       # True (공백만)
print(f"'ABC'.isupper()   : {'ABC'.isupper()}")       # True (대문자만)
print(f"'abc'.islower()   : {'abc'.islower()}")       # True (소문자만)

print()


# ============================================================
# 10. 문자열은 불변(Immutable)
# ============================================================
print("=== 불변성 ===")

s = "Hello"
# s[0] = "h"  # TypeError! 문자열은 변경할 수 없음

# 새로운 문자열을 만들어야 함
s_new = "h" + s[1:]
print(f"'{s}' → '{s_new}'")


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] 이메일 주소를 입력받아 @ 앞의 사용자 이름과 @ 뒤의 도메인을 분리해 출력하세요.
         예: "user@example.com" → 사용자: user, 도메인: example.com

[연습 2] 문자열 "Hello, World!"를 뒤집어서 출력하세요.
         슬라이싱을 활용하세요.

[연습 3] 주어진 문자열에서 특정 단어의 등장 횟수를 세는 프로그램을 작성하세요.
         text = "Python is great. Python is fun. Python is powerful."
         "Python"이 몇 번 등장하는지 출력하세요.

[연습 4] 주민등록번호 "900101-1234567"에서 뒷자리를 "*******"로 마스킹하세요.
         결과: "900101-*******"
"""

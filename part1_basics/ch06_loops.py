"""
Chapter 06: 반복문 (Loops)
============================
for, while 반복문과 제어문을 배웁니다.
"""

# ============================================================
# JavaScript vs Python 비교 - 반복문
# ============================================================
#
#  JavaScript                           Python
#  ─────────────────────────────────    ─────────────────────────────
#  for (let i = 0; i < 5; i++) {}      for i in range(5):
#  for (const item of arr) {}          for item in arr:    (for...of와 동일!)
#  for (const key in obj) {}           for key in dict:    (for...in과 유사)
#  while (조건) {}                     while 조건:
#  arr.forEach((item, i) => {})        for i, item in enumerate(arr):
#  arr.map(x => x * 2)                [x * 2 for x in arr]  (컴프리헨션)
#
#  break / continue                    break / continue    (동일!)
#
#  핵심 차이:
#  1) Python의 for는 항상 for...of 스타일 (C-style for 없음!)
#  2) range()로 숫자 시퀀스를 생성
#  3) for-else 문법이 존재 (JS에 없는 기능!)
#  4) Python에는 do-while 없음
#

# ============================================================
# 1. for 반복문 기초
# ============================================================
print("=== for 반복문 기초 ===")

# 리스트 순회 (JS의 for...of와 동일!)
# JS: for (const fruit of fruits) { console.log(fruit) }
fruits = ["사과", "바나나", "딸기", "포도"]
for fruit in fruits:
    print(f"과일: {fruit}")

print()

# 문자열 순회
for char in "Python":
    print(char, end=" ")
print()  # 줄바꿈

print()


# ============================================================
# 2. range() 함수
# ============================================================
print("=== range() ===")

# range(끝): 0부터 끝-1까지
# JS: for (let i = 0; i < 5; i++)  →  Python: for i in range(5)
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print()  # 0 1 2 3 4

# range(시작, 끝): 시작부터 끝-1까지
print("range(2, 7):", end=" ")
for i in range(2, 7):
    print(i, end=" ")
print()  # 2 3 4 5 6

# range(시작, 끝, 간격)
print("range(0, 10, 2):", end=" ")
for i in range(0, 10, 2):
    print(i, end=" ")
print()  # 0 2 4 6 8

# 역순
print("range(5, 0, -1):", end=" ")
for i in range(5, 0, -1):
    print(i, end=" ")
print()  # 5 4 3 2 1

print()


# ============================================================
# 3. for 반복문 활용
# ============================================================
print("=== for 활용 ===")

# 합계 구하기
total = 0
for i in range(1, 11):
    total += i
print(f"1~10 합계: {total}")    # 55

# 구구단
n = 5
print(f"\n{n}단:")
for i in range(1, 10):
    print(f"{n} × {i} = {n * i}")

print()


# ============================================================
# 4. enumerate() - 인덱스와 값을 함께
# ============================================================
print("=== enumerate() ===")

# JS의 forEach((item, index) => {})와 유사!
# JS: names.forEach((name, index) => console.log(index, name))
names = ["Alice", "Bob", "Charlie", "Diana"]

# 인덱스가 필요할 때
for index, name in enumerate(names):
    print(f"{index}번: {name}")

print()

# 시작 번호 지정
for rank, name in enumerate(names, start=1):
    print(f"{rank}등: {name}")

print()


# ============================================================
# 5. while 반복문
# ============================================================
print("=== while 반복문 ===")

# 기본 while
count = 1
while count <= 5:
    print(f"카운트: {count}")
    count += 1

print()

# 조건이 거짓이 될 때까지 반복
total = 0
number = 1
while total < 100:
    total += number
    number += 1
print(f"합이 100을 처음 넘는 시점: 1~{number - 1}까지의 합 = {total}")

print()


# ============================================================
# 6. break - 반복문 탈출
# ============================================================
print("=== break ===")

# 특정 값을 찾으면 멈추기
numbers = [4, 7, 2, 9, 1, 5, 8]
target = 9

for num in numbers:
    if num == target:
        print(f"찾았습니다: {target}")
        break
    print(f"{num}은(는) {target}이(가) 아닙니다.")

print()


# ============================================================
# 7. continue - 현재 반복 건너뛰기
# ============================================================
print("=== continue ===")

# 홀수만 출력
for i in range(1, 11):
    if i % 2 == 0:
        continue    # 짝수는 건너뛰기
    print(i, end=" ")
print()  # 1 3 5 7 9

print()


# ============================================================
# 8. for-else, while-else
# ============================================================
print("=== for-else ===")

# break 없이 정상 종료하면 else 블록 실행
numbers = [2, 4, 6, 8, 10]

for num in numbers:
    if num % 2 != 0:
        print(f"홀수 발견: {num}")
        break
else:
    print("홀수가 없습니다. 모두 짝수입니다!")

# break로 종료하면 else 블록 실행 안 됨
numbers = [2, 4, 5, 8, 10]

for num in numbers:
    if num % 2 != 0:
        print(f"홀수 발견: {num}")
        break
else:
    print("홀수가 없습니다.")

print()


# ============================================================
# 9. 중첩 반복문
# ============================================================
print("=== 중첩 반복문 ===")

# 구구단 전체 (2~5단만)
for i in range(2, 6):
    print(f"\n--- {i}단 ---")
    for j in range(1, 10):
        print(f"{i} × {j} = {i * j:2d}", end="  ")
    print()

print()

# 별 찍기
print("별 찍기:")
for i in range(1, 6):
    print("★" * i)

print()

# 역삼각형
for i in range(5, 0, -1):
    print(" " * (5 - i) + "★" * i)

print()


# ============================================================
# 10. 실전 예제: 소수 판별
# ============================================================
print("=== 실전 예제: 1~50 소수 찾기 ===")

primes = []
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print(f"1~50 사이의 소수: {primes}")
print(f"개수: {len(primes)}개")


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] 1부터 100까지의 숫자 중 3의 배수이면서 5의 배수인 수를 모두 출력하세요.

[연습 2] 사용자에게 정수를 입력받아 팩토리얼(n!)을 계산하세요.
         예: 5! = 5 × 4 × 3 × 2 × 1 = 120

[연습 3] 다음 패턴을 출력하세요:
         1
         1 2
         1 2 3
         1 2 3 4
         1 2 3 4 5

[연습 4] while문을 사용하여 사용자가 "quit"을 입력할 때까지
         반복해서 메시지를 입력받고 출력하는 프로그램을 작성하세요.
"""

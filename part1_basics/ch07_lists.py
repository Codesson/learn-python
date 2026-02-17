"""
Chapter 07: 리스트 (List)
===========================
파이썬에서 가장 많이 사용하는 자료구조인 리스트를 배웁니다.
"""

# ============================================================
# JavaScript vs Python 비교 - 리스트 (= JS의 Array)
# ============================================================
#
#  JavaScript (Array)                  Python (list)
#  ─────────────────────────────────  ─────────────────────────────
#  const arr = [1, 2, 3]             arr = [1, 2, 3]
#  arr.length                         len(arr)
#  arr.push(4)                        arr.append(4)
#  arr.pop()                          arr.pop()
#  arr.unshift(0)                     arr.insert(0, 0)
#  arr.shift()                        arr.pop(0)
#  arr.splice(1, 0, "new")           arr.insert(1, "new")
#  arr.splice(1, 1)                   del arr[1] 또는 arr.pop(1)
#  arr.indexOf(val)                   arr.index(val)
#  arr.includes(val)                  val in arr
#  arr.slice(1, 3)                    arr[1:3]           (슬라이싱!)
#  arr.concat(arr2)                   arr + arr2
#  arr.reverse()                      arr.reverse()
#  arr.sort()                         arr.sort()
#  arr.sort((a,b) => a-b)            arr.sort()  (기본이 오름차순)
#  [...arr] (스프레드)                arr.copy() 또는 arr[:]
#  arr.flat()                         (중첩 리스트 평탄화는 컴프리헨션으로)
#  arr.map(fn)                        [fn(x) for x in arr]
#  arr.filter(fn)                     [x for x in arr if fn(x)]
#  arr.reduce(fn, init)              functools.reduce(fn, arr, init)
#
#  핵심 차이: Python의 리스트는 JS Array와 거의 동일하게 사용!
#  다만 메서드 이름이 다르고, 슬라이싱 문법이 훨씬 강력합니다.
#

# ============================================================
# 1. 리스트 생성
# ============================================================
print("=== 리스트 생성 ===")

# 대괄호로 생성
fruits = ["사과", "바나나", "딸기"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]  # 다양한 타입 혼합 가능
empty = []

print(f"fruits: {fruits}")
print(f"numbers: {numbers}")
print(f"mixed: {mixed}")
print(f"empty: {empty}")

# list() 함수로 생성
chars = list("Python")              # ['P', 'y', 't', 'h', 'o', 'n']
nums = list(range(1, 6))            # [1, 2, 3, 4, 5]
print(f"chars: {chars}")
print(f"nums: {nums}")

print()


# ============================================================
# 2. 인덱싱과 슬라이싱
# ============================================================
print("=== 인덱싱 & 슬라이싱 ===")

colors = ["빨강", "주황", "노랑", "초록", "파랑", "남색", "보라"]

# 인덱싱
print(f"첫 번째: {colors[0]}")      # 빨강
print(f"마지막: {colors[-1]}")       # 보라
print(f"세 번째: {colors[2]}")       # 노랑

# 슬라이싱
print(f"처음 3개: {colors[:3]}")     # ['빨강', '주황', '노랑']
print(f"뒤에서 2개: {colors[-2:]}")  # ['남색', '보라']
print(f"짝수 인덱스: {colors[::2]}") # ['빨강', '노랑', '파랑', '보라']

# 리스트 값 변경 (문자열과 다르게 변경 가능!)
colors[0] = "빨간색"
print(f"변경 후: {colors}")

print()


# ============================================================
# 3. 리스트 추가/삭제
# ============================================================
print("=== 추가/삭제 ===")

animals = ["고양이", "강아지"]
print(f"초기: {animals}")

# 추가
animals.append("토끼")              # 끝에 추가     JS: push("토끼")
print(f"append('토끼'): {animals}")

animals.insert(1, "햄스터")          # 특정 위치에 삽입  JS: splice(1, 0, "햄스터")
print(f"insert(1, '햄스터'): {animals}")

animals.extend(["앵무새", "금붕어"])  # 여러 항목 추가  JS: push(...["앵무새", "금붕어"])
print(f"extend(): {animals}")

# 삭제
animals.remove("햄스터")             # 값으로 삭제 (첫 번째 일치 항목)
print(f"remove('햄스터'): {animals}")

popped = animals.pop()               # 마지막 항목 꺼내기
print(f"pop(): {popped}, 남은 리스트: {animals}")

popped = animals.pop(0)              # 특정 인덱스 항목 꺼내기
print(f"pop(0): {popped}, 남은 리스트: {animals}")

del animals[0]                        # del로 삭제
print(f"del [0]: {animals}")

# 전체 삭제
# animals.clear()

print()


# ============================================================
# 4. 리스트 검색
# ============================================================
print("=== 리스트 검색 ===")

scores = [85, 92, 78, 95, 88, 92, 76]

print(f"scores: {scores}")
print(f"92의 위치: {scores.index(92)}")          # 1 (첫 번째 위치)
print(f"92의 개수: {scores.count(92)}")           # 2
print(f"92가 있는가? {92 in scores}")             # True
print(f"100이 없는가? {100 not in scores}")       # True

print()


# ============================================================
# 5. 리스트 정렬
# ============================================================
print("=== 리스트 정렬 ===")

nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"원본: {nums}")

# sort(): 원본을 직접 정렬 (in-place)
nums.sort()
print(f"sort() 오름차순: {nums}")

nums.sort(reverse=True)
print(f"sort(reverse=True) 내림차순: {nums}")

# sorted(): 새로운 리스트를 반환 (원본 유지)
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(f"original: {original}")            # 변경 안 됨
print(f"sorted(): {sorted_list}")

# reverse(): 순서 뒤집기 (정렬이 아님)
nums = [3, 1, 4, 1, 5]
nums.reverse()
print(f"reverse(): {nums}")

# 문자열 정렬
names = ["Charlie", "Alice", "Bob", "Diana"]
names.sort()
print(f"문자열 정렬: {names}")

# 길이 기준 정렬
words = ["바나나", "사과", "딸기잼", "포도", "블루베리"]
words.sort(key=len)
print(f"길이 기준 정렬: {words}")

print()


# ============================================================
# 6. 리스트 연산
# ============================================================
print("=== 리스트 연산 ===")

a = [1, 2, 3]
b = [4, 5, 6]

# 연결
print(f"a + b = {a + b}")         # [1, 2, 3, 4, 5, 6]

# 반복
print(f"a * 3 = {a * 3}")         # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 길이
print(f"len(a) = {len(a)}")       # 3

# 최대/최소/합
nums = [10, 25, 8, 42, 17]
print(f"max: {max(nums)}, min: {min(nums)}, sum: {sum(nums)}")

print()


# ============================================================
# 7. 리스트 복사 (주의!)
# ============================================================
print("=== 리스트 복사 ===")

# 주의: 단순 대입은 참조 복사! (JS와 동일한 동작!)
# JS에서도 const b = a 하면 같은 배열을 참조하죠? 동일합니다.
original = [1, 2, 3]
reference = original       # 같은 리스트를 가리킴
reference[0] = 999
print(f"원본도 변경됨: {original}")     # [999, 2, 3]

# 얕은 복사 (shallow copy)
# JS: [...original], Array.from(original), original.slice()
original = [1, 2, 3]
copy1 = original.copy()   # 방법 1   JS: original.slice()
copy2 = original[:]       # 방법 2   JS: [...original] (스프레드와 유사)
copy3 = list(original)    # 방법 3   JS: Array.from(original)

copy1[0] = 999
print(f"원본 유지: {original}")         # [1, 2, 3]
print(f"복사본 변경: {copy1}")          # [999, 2, 3]

# 중첩 리스트의 깊은 복사
# JS: structuredClone(nested) 또는 JSON.parse(JSON.stringify(nested))
import copy
nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)
deep[0][0] = 999
print(f"원본 유지: {nested}")           # [[1, 2], [3, 4]]
print(f"깊은 복사 변경: {deep}")        # [[999, 2], [3, 4]]

print()


# ============================================================
# 8. 리스트 언패킹
# ============================================================
print("=== 리스트 언패킹 ===")

# 기본 언패킹 (JS의 구조 분해 할당과 유사!)
# JS: const [a, b, c] = [1, 2, 3]
a, b, c = [1, 2, 3]
print(f"a={a}, b={b}, c={c}")

# * 사용 (나머지 모두) - JS의 ...rest와 유사!
# JS: const [first, ...rest] = [1, 2, 3, 4, 5]
first, *rest = [1, 2, 3, 4, 5]
print(f"first={first}, rest={rest}")    # first=1, rest=[2, 3, 4, 5]

first, *middle, last = [1, 2, 3, 4, 5]
print(f"first={first}, middle={middle}, last={last}")

# 값 교환 (swap)
x, y = 10, 20
x, y = y, x
print(f"교환: x={x}, y={y}")           # x=20, y=10


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] 학생 5명의 점수를 리스트에 저장하고,
         평균 점수, 최고 점수, 최저 점수를 출력하세요.

[연습 2] 리스트에서 중복 요소를 제거하세요.
         예: [1, 2, 2, 3, 3, 3, 4] → [1, 2, 3, 4]

[연습 3] 두 개의 리스트를 합친 후 오름차순으로 정렬하세요.
         list1 = [3, 1, 8]
         list2 = [5, 2, 9]

[연습 4] 리스트의 요소를 역순으로 출력하는 3가지 방법을 작성하세요.
"""

"""
Chapter 08: 튜플 & 셋 (Tuple & Set)
======================================
불변 시퀀스 튜플과 집합 자료형 셋을 배웁니다.
"""

# ============================================================
# JavaScript vs Python 비교 - 튜플 & 셋
# ============================================================
#
#  튜플 (Tuple):
#  JS에는 튜플이 없습니다! Python 고유 자료형.
#  굳이 비유하면 Object.freeze([1, 2, 3])과 비슷한 "불변 배열"입니다.
#  함수에서 여러 값 반환 시 유용: return a, b  (JS: return { a, b } 또는 return [a, b])
#
#  셋 (Set):
#  JavaScript                      Python
#  ─────────────────────────────    ─────────────────────────────
#  new Set([1, 2, 3])              {1, 2, 3}
#  set.add(4)                      set.add(4)          (동일!)
#  set.delete(4)                   set.remove(4) 또는 set.discard(4)
#  set.has(4)                      4 in set            (in 연산자!)
#  set.size                        len(set)
#  set.clear()                     set.clear()         (동일!)
#
#  Python만의 강력한 기능:
#  set_a | set_b  (합집합)         JS: 직접 구현 필요
#  set_a & set_b  (교집합)         JS: 직접 구현 필요
#  set_a - set_b  (차집합)         JS: 직접 구현 필요
#  → Python의 Set은 수학적 집합 연산을 기본 지원합니다!
#

# ============================================================
# 1. 튜플 (Tuple) 기초
# ============================================================
print("=== 튜플 기초 ===")

# 소괄호로 생성
point = (3, 4)
colors = ("빨강", "초록", "파랑")
single = (42,)       # 요소가 하나일 때 반드시 콤마 필요!
not_tuple = (42)     # 이건 그냥 정수!

print(f"point: {point}, type: {type(point)}")
print(f"colors: {colors}")
print(f"single: {single}, type: {type(single)}")
print(f"not_tuple: {not_tuple}, type: {type(not_tuple)}")

# 괄호 없이도 생성 가능
another = 1, 2, 3
print(f"another: {another}, type: {type(another)}")

print()


# ============================================================
# 2. 튜플 인덱싱/슬라이싱 (리스트와 동일)
# ============================================================
print("=== 튜플 인덱싱 ===")

fruits = ("사과", "바나나", "딸기", "포도", "수박")

print(f"fruits[0]: {fruits[0]}")
print(f"fruits[-1]: {fruits[-1]}")
print(f"fruits[1:3]: {fruits[1:3]}")

# 하지만 값 변경은 불가! (불변)
# fruits[0] = "오렌지"  # TypeError!

print()


# ============================================================
# 3. 튜플은 왜 사용하는가?
# ============================================================
print("=== 튜플의 활용 ===")

# 1) 함수에서 여러 값 반환
def get_min_max(numbers):
    return min(numbers), max(numbers)

result = get_min_max([3, 1, 4, 1, 5, 9])
print(f"결과: {result}")              # (1, 9)
minimum, maximum = result             # 언패킹
print(f"최소: {minimum}, 최대: {maximum}")

# 2) 딕셔너리의 키로 사용 가능 (리스트는 불가!)
locations = {
    (37.5665, 126.978): "서울",
    (35.1796, 129.0756): "부산",
}
print(f"(37.5665, 126.978) → {locations[(37.5665, 126.978)]}")

# 3) 값 교환
a, b = 10, 20
a, b = b, a    # 사실 이것도 튜플!
print(f"교환 결과: a={a}, b={b}")

# 4) 튜플 메서드
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"\ncount(2): {numbers.count(2)}")    # 3
print(f"index(3): {numbers.index(3)}")      # 2

print()


# ============================================================
# 4. 튜플 ↔ 리스트 변환
# ============================================================
print("=== 변환 ===")

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(f"리스트 → 튜플: {my_tuple}")

back_to_list = list(my_tuple)
print(f"튜플 → 리스트: {back_to_list}")

print()


# ============================================================
# 5. 셋 (Set) 기초
# ============================================================
print("=" * 40)
print("=== 셋 (Set) 기초 ===")

# 중괄호로 생성 (중복 자동 제거, 순서 없음)
fruits = {"사과", "바나나", "딸기", "사과", "바나나"}
print(f"fruits: {fruits}")     # 중복 제거됨!

numbers = {3, 1, 4, 1, 5, 9, 2, 6}
print(f"numbers: {numbers}")   # 순서가 보장되지 않음

# 빈 셋 만들기 (주의: {}는 빈 딕셔너리!)
empty_set = set()              # 올바른 방법
empty_dict = {}                # 이건 딕셔너리!
print(f"type(set()): {type(empty_set)}")
print(f"type({{}}):   {type(empty_dict)}")

# set()으로 생성
char_set = set("hello")
print(f"set('hello'): {char_set}")    # {'h', 'e', 'l', 'o'}

print()


# ============================================================
# 6. 셋 추가/삭제
# ============================================================
print("=== 셋 추가/삭제 ===")

s = {1, 2, 3}
print(f"초기: {s}")

s.add(4)
print(f"add(4): {s}")

s.add(3)           # 이미 있으면 무시
print(f"add(3): {s}")

s.update([5, 6, 7])  # 여러 항목 추가
print(f"update([5,6,7]): {s}")

s.remove(7)        # 값으로 삭제 (없으면 KeyError)
print(f"remove(7): {s}")

s.discard(99)      # 값으로 삭제 (없어도 에러 없음)
print(f"discard(99): {s}")

popped = s.pop()   # 임의의 항목 꺼내기
print(f"pop(): {popped}, 남은 셋: {s}")

print()


# ============================================================
# 7. 집합 연산 (셋의 핵심!)
# ============================================================
print("=== 집합 연산 ===")

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"A = {a}")
print(f"B = {b}")

# 합집합 (Union)
print(f"A | B (합집합)  = {a | b}")            # {1,2,3,4,5,6,7,8}
print(f"A.union(B)      = {a.union(b)}")

# 교집합 (Intersection)
print(f"A & B (교집합)  = {a & b}")            # {4, 5}
print(f"A.intersection(B) = {a.intersection(b)}")

# 차집합 (Difference)
print(f"A - B (차집합)  = {a - b}")            # {1, 2, 3}
print(f"B - A (차집합)  = {b - a}")            # {6, 7, 8}

# 대칭 차집합 (Symmetric Difference)
print(f"A ^ B (대칭차)  = {a ^ b}")            # {1, 2, 3, 6, 7, 8}

print()


# ============================================================
# 8. 부분집합 / 상위집합
# ============================================================
print("=== 부분집합/상위집합 ===")

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(f"A = {a}")
print(f"B = {b}")
print(f"A ⊂ B (부분집합)? {a.issubset(b)}")       # True
print(f"B ⊃ A (상위집합)? {b.issuperset(a)}")     # True
print(f"A와 B 서로소?   {a.isdisjoint({6, 7})}")  # True (공통 원소 없음)

print()


# ============================================================
# 9. 실전 예제: 중복 제거 & 공통 요소 찾기
# ============================================================
print("=== 실전 예제 ===")

# 중복 제거
scores = [85, 92, 78, 85, 90, 92, 88]
unique_scores = list(set(scores))
print(f"원본: {scores}")
print(f"중복 제거: {unique_scores}")

# 공통 수강 과목 찾기
student_a = {"수학", "영어", "물리", "화학"}
student_b = {"영어", "화학", "생물", "지구과학"}

common = student_a & student_b
only_a = student_a - student_b
only_b = student_b - student_a

print(f"\n학생A 과목: {student_a}")
print(f"학생B 과목: {student_b}")
print(f"공통 과목: {common}")
print(f"A만 수강: {only_a}")
print(f"B만 수강: {only_b}")


# ============================================================
# 10. frozenset (불변 셋)
# ============================================================
print("\n=== frozenset ===")

fs = frozenset([1, 2, 3, 4])
print(f"frozenset: {fs}")
# fs.add(5)  # AttributeError! (불변이므로 추가 불가)

# 딕셔너리 키나 셋의 원소로 사용 가능
d = {frozenset([1, 2]): "그룹A"}
print(f"frozenset을 키로: {d}")


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] 두 리스트의 공통 요소를 셋을 이용하여 찾으세요.
         list1 = [1, 2, 3, 4, 5, 6]
         list2 = [4, 5, 6, 7, 8, 9]

[연습 2] 문자열에서 사용된 고유한 문자의 개수를 셋을 이용하여 구하세요.
         text = "hello world"

[연습 3] 좌표 (x, y)를 튜플로 표현하고,
         두 좌표 사이의 거리를 계산하는 함수를 작성하세요.
         (힌트: 유클리드 거리 = √((x2-x1)² + (y2-y1)²))
"""

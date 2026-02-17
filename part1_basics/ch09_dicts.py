"""
Chapter 09: 딕셔너리 (Dictionary)
===================================
키-값 쌍으로 데이터를 저장하는 딕셔너리를 배웁니다.
"""

# ============================================================
# JavaScript vs Python 비교 - 딕셔너리 (= JS의 Object / Map)
# ============================================================
#
#  JavaScript (Object)               Python (dict)
#  ─────────────────────────────────  ─────────────────────────────
#  const obj = {name: "홍길동"}      d = {"name": "홍길동"}  (키에 따옴표 필수!)
#  obj.name 또는 obj["name"]         d["name"]  (dot 접근 불가!)
#  obj.name = "이영희"               d["name"] = "이영희"
#  delete obj.name                   del d["name"]
#  "name" in obj                     "name" in d           (동일!)
#  Object.keys(obj)                  d.keys()
#  Object.values(obj)                d.values()
#  Object.entries(obj)               d.items()
#  for (const [k,v] of entries)      for k, v in d.items():
#  {...obj1, ...obj2}                {**d1, **d2} 또는 d1 | d2  (3.9+)
#  obj?.name (옵셔널 체이닝)          d.get("name")  (없으면 None 반환)
#
#  핵심 차이:
#  1) Python dict의 키에는 반드시 따옴표가 필요 (JS 객체는 선택)
#  2) dot 접근(obj.key)이 불가하고 반드시 d["key"] 사용
#  3) d.get("key")로 안전하게 접근 (JS의 ?. 대용)
#  4) Python dict는 JS의 Map과 더 유사 (삽입 순서 보장, 다양한 키 타입)
#

# ============================================================
# 1. 딕셔너리 생성
# ============================================================
print("=== 딕셔너리 생성 ===")

# 중괄호로 생성
person = {
    "name": "홍길동",
    "age": 25,
    "city": "서울"
}
print(f"person: {person}")

# dict() 함수로 생성
person2 = dict(name="이영희", age=30, city="부산")
print(f"person2: {person2}")

# 빈 딕셔너리
empty = {}
empty2 = dict()
print(f"빈 딕셔너리: {empty}")

# 리스트 of 튜플로 생성
items = dict([("apple", 1000), ("banana", 500)])
print(f"items: {items}")

print()


# ============================================================
# 2. 값 접근 및 수정
# ============================================================
print("=== 값 접근/수정 ===")

student = {
    "name": "김철수",
    "age": 20,
    "scores": [85, 92, 78]
}

# 값 접근
print(f"이름: {student['name']}")
print(f"나이: {student['age']}")
print(f"점수: {student['scores']}")

# get() - 키가 없을 때 안전하게 접근 (JS의 ?. 옵셔널 체이닝 대용!)
# JS: student?.school ?? "미정"
# Python: student.get("school", "미정")
print(f"이름: {student.get('name')}")
print(f"학교: {student.get('school')}")           # None (에러 없음)
print(f"학교: {student.get('school', '미정')}")   # '미정' (기본값 지정)

# 값 수정
student["age"] = 21
print(f"나이 변경: {student['age']}")

# 새 키-값 추가
student["school"] = "서울대"
student["grade"] = "A"
print(f"추가 후: {student}")

print()


# ============================================================
# 3. 딕셔너리 삭제
# ============================================================
print("=== 삭제 ===")

menu = {
    "아메리카노": 4000,
    "라떼": 4500,
    "카푸치노": 5000,
    "모카": 5500
}
print(f"원본: {menu}")

# del: 키로 삭제
del menu["카푸치노"]
print(f"del '카푸치노': {menu}")

# pop(): 값을 반환하면서 삭제
price = menu.pop("라떼")
print(f"pop('라떼'): {price}, 남은 메뉴: {menu}")

# pop(): 없는 키에 기본값 설정
result = menu.pop("에스프레소", "없는 메뉴")
print(f"pop('에스프레소', 기본값): {result}")

# popitem(): 마지막 항목 꺼내기
item = menu.popitem()
print(f"popitem(): {item}")

print()


# ============================================================
# 4. 딕셔너리 순회
# ============================================================
print("=== 딕셔너리 순회 ===")

scores = {
    "수학": 95,
    "영어": 88,
    "과학": 92,
    "국어": 85
}

# 키 순회 (기본)
print("--- 키 순회 ---")
for subject in scores:
    print(f"{subject}: {scores[subject]}")

# keys() 메서드
print(f"\n키 목록: {list(scores.keys())}")

# values() 메서드
print(f"값 목록: {list(scores.values())}")

# items() 메서드 (키, 값 동시 순회 - 가장 많이 사용!)
# JS: for (const [subject, score] of Object.entries(scores))
print("\n--- items() 순회 ---")
for subject, score in scores.items():
    print(f"{subject}: {score}점")

# 평균 계산
average = sum(scores.values()) / len(scores)
print(f"\n평균 점수: {average:.1f}점")

print()


# ============================================================
# 5. 딕셔너리 메서드
# ============================================================
print("=== 딕셔너리 메서드 ===")

d = {"a": 1, "b": 2, "c": 3}

# update(): 다른 딕셔너리 병합
d.update({"c": 30, "d": 4})     # 겹치면 덮어쓰기
print(f"update(): {d}")

# setdefault(): 키가 없을 때만 추가
d.setdefault("e", 5)    # "e"가 없으므로 추가
d.setdefault("a", 99)   # "a"가 있으므로 무시
print(f"setdefault(): {d}")

# 키 존재 확인
print(f"'a' in d: {'a' in d}")       # True
print(f"'z' in d: {'z' in d}")       # False

print()


# ============================================================
# 6. 딕셔너리 병합 (파이썬 3.9+)
# ============================================================
print("=== 딕셔너리 병합 (3.9+) ===")

default = {"theme": "light", "lang": "ko", "font_size": 14}
custom = {"theme": "dark", "font_size": 16}

# | 연산자: 병합 (오른쪽이 우선)
# JS의 스프레드와 동일: {...default, ...custom}
merged = default | custom
print(f"merged: {merged}")

# |= 연산자: 업데이트
settings = {"theme": "light"}
settings |= {"theme": "dark", "lang": "en"}
print(f"settings: {settings}")

print()


# ============================================================
# 7. 중첩 딕셔너리
# ============================================================
print("=== 중첩 딕셔너리 ===")

students = {
    "학생1": {
        "name": "김철수",
        "scores": {"수학": 95, "영어": 88}
    },
    "학생2": {
        "name": "이영희",
        "scores": {"수학": 82, "영어": 95}
    }
}

# 중첩 접근
print(f"학생1 이름: {students['학생1']['name']}")
print(f"학생2 수학 점수: {students['학생2']['scores']['수학']}")

# 중첩 순회
for student_id, info in students.items():
    print(f"\n{student_id}: {info['name']}")
    for subject, score in info["scores"].items():
        print(f"  {subject}: {score}점")

print()


# ============================================================
# 8. 실전 예제: 단어 빈도수 세기
# ============================================================
print("=== 실전 예제: 단어 빈도수 ===")

text = "apple banana apple cherry banana apple cherry cherry cherry"
words = text.split()

# 방법 1: 직접 세기
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(f"방법1: {word_count}")

# 방법 2: get() 활용
word_count2 = {}
for word in words:
    word_count2[word] = word_count2.get(word, 0) + 1
print(f"방법2: {word_count2}")

# 방법 3: collections.Counter 사용
from collections import Counter
word_count3 = Counter(words)
print(f"방법3: {dict(word_count3)}")
print(f"가장 많은 2개: {word_count3.most_common(2)}")

print()


# ============================================================
# 9. 실전 예제: 전화번호부
# ============================================================
print("=== 실전 예제: 전화번호부 ===")

phonebook = {}

# 추가
phonebook["홍길동"] = "010-1234-5678"
phonebook["이영희"] = "010-2345-6789"
phonebook["김철수"] = "010-3456-7890"

# 검색
name = "이영희"
if name in phonebook:
    print(f"{name}: {phonebook[name]}")
else:
    print(f"{name}을(를) 찾을 수 없습니다.")

# 전체 출력
print("\n--- 전화번호부 ---")
for name, phone in sorted(phonebook.items()):
    print(f"{name}: {phone}")


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] 학생 이름을 키, 점수를 값으로 하는 딕셔너리를 만들고,
         평균 이상인 학생만 출력하세요.

[연습 2] 문장에서 각 알파벳의 등장 횟수를 딕셔너리로 만드세요.
         (공백 제외, 대소문자 구분 없이)

[연습 3] 두 딕셔너리를 받아서 공통 키와 그 값을 출력하는 함수를 작성하세요.
"""

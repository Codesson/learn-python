"""
Chapter 11: 파일 입출력 (File I/O)
====================================
파일 읽기, 쓰기, 그리고 with 문을 배웁니다.
"""

# ============================================================
# JavaScript vs Python 비교 - 파일 I/O
# ============================================================
#
#  Node.js (fs 모듈)                  Python
#  ─────────────────────────────────  ─────────────────────────────
#  fs.readFileSync(path, 'utf8')     open(path).read()
#  fs.writeFileSync(path, data)      open(path, 'w').write(data)
#  fs.appendFileSync(path, data)     open(path, 'a').write(data)
#  fs.existsSync(path)               os.path.exists(path)
#  fs.unlinkSync(path)               os.remove(path)
#  fs.readdirSync(dir)               os.listdir(dir)
#  JSON.parse(str)                   json.loads(str)
#  JSON.stringify(obj)               json.dumps(obj)
#
#  핵심 차이:
#  1) Python은 with문으로 자동 리소스 해제 (Node의 try-finally 대용)
#  2) Node는 비동기가 기본, Python은 동기가 기본
#  3) CSV 처리가 Python 표준 라이브러리에 내장 (Node는 외부 패키지)
#

import os

# 예제 파일을 저장할 디렉토리
os.makedirs("temp_files", exist_ok=True)


# ============================================================
# 1. 파일 쓰기 (write)
# ============================================================
print("=== 파일 쓰기 ===")

# 'w' 모드: 쓰기 (파일이 있으면 덮어쓰기)
f = open("temp_files/hello.txt", "w", encoding="utf-8")
f.write("안녕하세요!\n")
f.write("파이썬 파일 입출력을 배우고 있습니다.\n")
f.write("파일 쓰기 완료!\n")
f.close()
print("hello.txt 파일 생성 완료!")

# writelines(): 리스트를 한 번에 쓰기
lines = ["첫 번째 줄\n", "두 번째 줄\n", "세 번째 줄\n"]
f = open("temp_files/lines.txt", "w", encoding="utf-8")
f.writelines(lines)
f.close()
print("lines.txt 파일 생성 완료!")

print()


# ============================================================
# 2. 파일 읽기 (read)
# ============================================================
print("=== 파일 읽기 ===")

# read(): 전체 읽기
f = open("temp_files/hello.txt", "r", encoding="utf-8")
content = f.read()
f.close()
print("--- read() ---")
print(content)

# readline(): 한 줄씩 읽기
f = open("temp_files/hello.txt", "r", encoding="utf-8")
print("--- readline() ---")
line = f.readline()
while line:
    print(line, end="")  # 이미 줄바꿈이 포함되어 있음
    line = f.readline()
f.close()
print()

# readlines(): 모든 줄을 리스트로 읽기
f = open("temp_files/hello.txt", "r", encoding="utf-8")
all_lines = f.readlines()
f.close()
print("--- readlines() ---")
print(all_lines)

print()


# ============================================================
# 3. with 문 (Context Manager) - 권장!
# ============================================================
print("=== with 문 (권장) ===")

# with를 사용하면 자동으로 close() 호출!
# Node.js에서는 try-finally로 fd.close()를 보장하지만,
# Python의 with문은 이를 자동으로 처리합니다. (Context Manager)
with open("temp_files/hello.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# for문으로 한 줄씩 읽기 (메모리 효율적)
print("--- for문으로 읽기 ---")
with open("temp_files/hello.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # strip()으로 줄바꿈 제거

print()


# ============================================================
# 4. 파일 추가 모드 (append)
# ============================================================
print("=== 추가 모드 ===")

# 'a' 모드: 기존 내용 유지하고 끝에 추가
with open("temp_files/hello.txt", "a", encoding="utf-8") as f:
    f.write("추가된 줄입니다.\n")
    f.write("또 하나 추가!\n")

with open("temp_files/hello.txt", "r", encoding="utf-8") as f:
    print(f.read())


# ============================================================
# 5. 파일 모드 정리
# ============================================================
"""
파일 모드 정리:
  'r'  : 읽기 (기본값, 파일이 없으면 에러)
  'w'  : 쓰기 (파일이 있으면 덮어쓰기, 없으면 생성)
  'a'  : 추가 (파일 끝에 추가, 없으면 생성)
  'x'  : 생성 (파일이 이미 있으면 에러)
  'b'  : 바이너리 모드 (예: 'rb', 'wb')
  '+'  : 읽기+쓰기 (예: 'r+', 'w+')
"""


# ============================================================
# 6. CSV 파일 다루기
# ============================================================
print("=== CSV 파일 ===")
import csv

# CSV 쓰기
students = [
    ["이름", "나이", "점수"],
    ["홍길동", 25, 95],
    ["이영희", 23, 88],
    ["김철수", 27, 92],
]

with open("temp_files/students.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)
print("students.csv 생성 완료!")

# CSV 읽기
with open("temp_files/students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print()

# DictReader / DictWriter (딕셔너리 형태)
print("--- DictReader ---")
with open("temp_files/students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['이름']} - 점수: {row['점수']}")

print()


# ============================================================
# 7. JSON 파일 다루기
# ============================================================
print("=== JSON 파일 ===")
import json

# JSON 쓰기
# JS: JSON.stringify(data)  →  Python: json.dumps(data)
# JS: JSON.parse(str)       →  Python: json.loads(str)
data = {
    "name": "홍길동",
    "age": 25,
    "scores": [95, 88, 92],
    "address": {
        "city": "서울",
        "district": "강남구"
    }
}

with open("temp_files/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("data.json 생성 완료!")

# JSON 읽기
with open("temp_files/data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(f"이름: {loaded['name']}")
print(f"점수: {loaded['scores']}")
print(f"도시: {loaded['address']['city']}")

# 문자열 ↔ JSON
json_string = json.dumps(data, ensure_ascii=False)
print(f"\nJSON 문자열: {json_string}")

parsed = json.loads(json_string)
print(f"파싱 결과: {parsed['name']}")

print()


# ============================================================
# 8. os / os.path - 파일/디렉토리 조작
# ============================================================
print("=== os 모듈 ===")

# 현재 작업 디렉토리
print(f"현재 디렉토리: {os.getcwd()}")

# 파일 존재 여부
print(f"hello.txt 존재: {os.path.exists('temp_files/hello.txt')}")
print(f"없는파일 존재: {os.path.exists('temp_files/없는파일.txt')}")

# 파일/디렉토리 구분
print(f"hello.txt은 파일? {os.path.isfile('temp_files/hello.txt')}")
print(f"temp_files는 디렉토리? {os.path.isdir('temp_files')}")

# 파일 크기
size = os.path.getsize("temp_files/hello.txt")
print(f"hello.txt 크기: {size} bytes")

# 디렉토리 내 파일 목록
print(f"temp_files 내용: {os.listdir('temp_files')}")


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] 사용자에게 여러 줄의 텍스트를 입력받아 파일로 저장하세요.
         빈 줄을 입력하면 저장을 종료합니다.

[연습 2] CSV 파일에서 점수 데이터를 읽어 평균을 계산하세요.
         (students.csv 파일을 활용)

[연습 3] JSON 파일에 할 일 목록을 저장/불러오기 하는
         간단한 TODO 프로그램을 작성하세요.
"""

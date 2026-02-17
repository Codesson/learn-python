"""
Chapter 17: pandas 데이터 가공
================================
필터링, 그룹화, 결측치, 병합 등 데이터 전처리를 배웁니다.
"""

import pandas as pd
import numpy as np

# 예제 데이터 생성
np.random.seed(42)

df = pd.DataFrame({
    "이름": ["홍길동", "이영희", "김철수", "박지민", "최수연",
            "정다은", "한민수", "오서연", "윤재호", "강하늘"],
    "부서": ["영업", "개발", "영업", "개발", "마케팅",
            "개발", "영업", "마케팅", "개발", "영업"],
    "연차": [3, 5, 1, 7, 2, 4, 6, 3, 2, 8],
    "급여": [3500, 5000, 2800, 6200, 3200,
            4500, 5500, 3800, 3000, 6000],
    "평가": ["B", "A", "C", "A", "B", "A", "B", "A", "C", "A"]
})

print("=== 원본 데이터 ===")
print(df)
print()


# ============================================================
# 1. apply() - 함수 적용
# ============================================================
print("=== apply() ===")

# 컬럼에 함수 적용
df["급여등급"] = df["급여"].apply(lambda x: "높음" if x >= 5000 else ("보통" if x >= 3500 else "낮음"))
print("급여등급 추가:")
print(df[["이름", "급여", "급여등급"]])

# 여러 컬럼을 사용하는 apply (axis=1: 행 단위)
def classify(row):
    if row["연차"] >= 5 and row["평가"] == "A":
        return "핵심인재"
    elif row["평가"] == "A":
        return "우수"
    else:
        return "일반"

df["분류"] = df.apply(classify, axis=1)
print(f"\n인재 분류:")
print(df[["이름", "연차", "평가", "분류"]])

print()


# ============================================================
# 2. groupby() - 그룹화
# ============================================================
print("=== groupby() ===")

# 부서별 평균 급여
print("--- 부서별 평균 급여 ---")
print(df.groupby("부서")["급여"].mean())

# 부서별 여러 통계
print("\n--- 부서별 통계 ---")
print(df.groupby("부서")["급여"].agg(["mean", "min", "max", "count"]))

# 여러 컬럼으로 그룹화
print("\n--- 부서별/평가별 평균 급여 ---")
print(df.groupby(["부서", "평가"])["급여"].mean())

# agg()로 컬럼마다 다른 연산
print("\n--- 부서별 종합 통계 ---")
result = df.groupby("부서").agg({
    "급여": ["mean", "sum"],
    "연차": "mean",
    "이름": "count"
})
print(result)

print()


# ============================================================
# 3. 결측치 (Missing Data) 처리
# ============================================================
print("=== 결측치 처리 ===")

# 결측치가 있는 데이터 생성
df_missing = pd.DataFrame({
    "이름": ["A", "B", "C", "D", "E"],
    "나이": [25, np.nan, 30, np.nan, 28],
    "점수": [85, 92, np.nan, 78, np.nan],
    "도시": ["서울", "부산", None, "대구", "서울"]
})
print("결측치 포함 데이터:")
print(df_missing)

# 결측치 확인
print(f"\n결측치 개수:\n{df_missing.isnull().sum()}")
print(f"\n결측치 존재 여부:\n{df_missing.isnull().any()}")
print(f"전체 결측치 수: {df_missing.isnull().sum().sum()}")

# 결측치 제거
print("\n--- dropna() ---")
print(df_missing.dropna())                       # 결측치 있는 행 전체 삭제
print()
print(df_missing.dropna(subset=["나이"]))          # 특정 컬럼 기준

# 결측치 채우기
print("\n--- fillna() ---")
df_filled = df_missing.copy()
df_filled["나이"] = df_filled["나이"].fillna(df_filled["나이"].mean())
df_filled["점수"] = df_filled["점수"].fillna(0)
df_filled["도시"] = df_filled["도시"].fillna("미상")
print(df_filled)

print()


# ============================================================
# 4. 데이터 변환
# ============================================================
print("=== 데이터 변환 ===")

# replace(): 값 치환
df_temp = df.copy()
df_temp["평가"] = df_temp["평가"].replace({"A": "우수", "B": "보통", "C": "미흡"})
print("평가 치환:")
print(df_temp[["이름", "평가"]])

# map(): Series 값 매핑
grade_map = {"A": 4.0, "B": 3.0, "C": 2.0}
df["평가점수"] = df["평가"].map(grade_map)
print(f"\n평가점수 추가:")
print(df[["이름", "평가", "평가점수"]])

# 문자열 메서드
names = pd.Series(["  hello  ", "WORLD", "PyThOn"])
print(f"\nstrip: {names.str.strip().tolist()}")
print(f"lower: {names.str.lower().tolist()}")
print(f"upper: {names.str.upper().tolist()}")

print()


# ============================================================
# 5. 데이터 병합 (merge, concat)
# ============================================================
print("=== 데이터 병합 ===")

# 두 DataFrame 준비
employees = pd.DataFrame({
    "사원ID": [1, 2, 3, 4, 5],
    "이름": ["홍길동", "이영희", "김철수", "박지민", "최수연"]
})

salaries = pd.DataFrame({
    "사원ID": [1, 2, 3, 4, 6],
    "급여": [3500, 5000, 2800, 6200, 4000]
})

print("employees:")
print(employees)
print("\nsalaries:")
print(salaries)

# merge (SQL JOIN과 동일)
# inner join (기본): 양쪽 모두 있는 것만
print("\n--- inner join ---")
print(pd.merge(employees, salaries, on="사원ID"))

# left join: 왼쪽 기준
print("\n--- left join ---")
print(pd.merge(employees, salaries, on="사원ID", how="left"))

# outer join: 모두 포함
print("\n--- outer join ---")
print(pd.merge(employees, salaries, on="사원ID", how="outer"))

# concat: 단순 연결
print("\n--- concat (행 연결) ---")
df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
print(pd.concat([df1, df2], ignore_index=True))

print()


# ============================================================
# 6. 피벗 테이블
# ============================================================
print("=== 피벗 테이블 ===")

# 예제 데이터
sales = pd.DataFrame({
    "날짜": ["월", "월", "화", "화", "수", "수"] * 2,
    "상품": ["A", "B"] * 6,
    "수량": [10, 20, 15, 25, 12, 18, 8, 22, 14, 28, 11, 16]
})

# 피벗 테이블
pivot = pd.pivot_table(
    sales,
    values="수량",
    index="날짜",
    columns="상품",
    aggfunc="sum"
)
print("피벗 테이블:")
print(pivot)

print()


# ============================================================
# 7. 날짜/시간 데이터
# ============================================================
print("=== 날짜/시간 처리 ===")

# 날짜 컬럼 생성
dates = pd.date_range("2025-01-01", periods=10, freq="D")
ts = pd.DataFrame({
    "날짜": dates,
    "값": np.random.randint(100, 200, 10)
})
print(ts)

# 날짜 속성 접근
ts["요일"] = ts["날짜"].dt.day_name()
ts["월"] = ts["날짜"].dt.month
ts["일"] = ts["날짜"].dt.day
print(f"\n날짜 속성 추가:")
print(ts)

print()


# ============================================================
# 8. 실전 예제: 종합 데이터 분석
# ============================================================
print("=== 실전 예제: 종합 분석 ===")

# 부서별 분석
print("--- 부서별 분석 ---")
dept_summary = df.groupby("부서").agg(
    인원수=("이름", "count"),
    평균급여=("급여", "mean"),
    평균연차=("연차", "mean"),
    우수비율=("평가", lambda x: (x == "A").mean() * 100)
).round(1)
print(dept_summary)

# 급여 구간별 분포
print("\n--- 급여 구간별 분포 ---")
bins = [0, 3000, 4000, 5000, 7000]
labels = ["3천 미만", "3~4천", "4~5천", "5천 이상"]
df["급여구간"] = pd.cut(df["급여"], bins=bins, labels=labels)
print(df["급여구간"].value_counts().sort_index())

# 최종 데이터
print("\n--- 최종 데이터 ---")
print(df[["이름", "부서", "급여", "급여구간", "평가", "분류"]].to_string(index=False))


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] 학생 성적 데이터를 만들고, 과목별 평균/최고/최저 점수를
         groupby로 구하세요.

[연습 2] 결측치가 포함된 데이터를 만들고, 다양한 방법으로
         결측치를 처리해 보세요 (삭제, 평균으로 채우기, 앞/뒤 값으로 채우기).

[연습 3] 두 개의 CSV 파일을 merge하여 하나의 DataFrame으로
         합치고 분석하세요.
"""

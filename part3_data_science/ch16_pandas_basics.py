"""
Chapter 16: pandas 기초
=========================
데이터 분석의 핵심 라이브러리 pandas의 기본을 배웁니다.
실행 전: pip install pandas
"""

# ============================================================
# JavaScript 개발자를 위한 pandas 안내
# ============================================================
#
#  pandas는 JS 생태계에 직접적인 대응이 없는 Python의 킬러 라이브러리입니다.
#  굳이 비유하면:
#
#  - DataFrame ≈ 엑셀 스프레드시트를 코드로 다루는 것
#  - DataFrame ≈ SQL 테이블을 메모리에 올려놓은 것
#  - JS에서 배열 of 객체 [{...}, {...}]를 다루는 것과 유사하지만,
#    내장 필터링/정렬/통계 기능이 훨씬 강력합니다.
#
#  JS 유사 라이브러리: Danfo.js, Arquero (하지만 pandas만큼 강력하지 않음)
#
#  자주 쓰는 패턴 비교:
#  JS: data.filter(d => d.age > 20)
#  pandas: df[df["age"] > 20]
#
#  JS: data.map(d => ({...d, bonus: d.score * 10}))
#  pandas: df["bonus"] = df["score"] * 10
#
#  JS: data.reduce((sum, d) => sum + d.score, 0) / data.length
#  pandas: df["score"].mean()
#

import pandas as pd
import numpy as np

# ============================================================
# 1. Series (1차원 데이터)
# ============================================================
print("=== Series 기초 ===")

# 리스트로 Series 생성
s = pd.Series([10, 20, 30, 40, 50])
print(s)
print(f"\ntype: {type(s)}")
print(f"값: {s.values}")
print(f"인덱스: {s.index.tolist()}")

# 인덱스 지정
scores = pd.Series(
    [95, 88, 92, 78, 85],
    index=["수학", "영어", "과학", "국어", "사회"]
)
print(f"\n점수:\n{scores}")
print(f"\n수학 점수: {scores['수학']}")
print(f"평균: {scores.mean():.1f}")

# 딕셔너리로 Series 생성
population = pd.Series({
    "서울": 9720,
    "부산": 3404,
    "대구": 2438,
    "인천": 2955,
})
print(f"\n인구(만명):\n{population}")

print()


# ============================================================
# 2. DataFrame 생성
# ============================================================
print("=" * 50)
print("=== DataFrame 기초 ===")

# 딕셔너리로 생성 (가장 일반적)
data = {
    "이름": ["홍길동", "이영희", "김철수", "박지민", "최수연"],
    "나이": [25, 30, 22, 28, 35],
    "도시": ["서울", "부산", "서울", "대구", "인천"],
    "점수": [85, 92, 78, 95, 88]
}

df = pd.DataFrame(data)
print(df)
print(f"\ntype: {type(df)}")
print(f"shape: {df.shape}")          # (행, 열)
print(f"columns: {df.columns.tolist()}")
print(f"dtypes:\n{df.dtypes}")

print()


# ============================================================
# 3. DataFrame 기본 정보 확인
# ============================================================
print("=== DataFrame 정보 ===")

print("--- head() / tail() ---")
print(df.head(3))       # 처음 3행
print(df.tail(2))       # 마지막 2행

print("\n--- info() ---")
df.info()               # 컬럼 정보, 타입, null 개수

print("\n--- describe() ---")
print(df.describe())    # 기술 통계 (숫자 컬럼만)

print()


# ============================================================
# 4. 컬럼/행 접근
# ============================================================
print("=== 데이터 접근 ===")

# 컬럼 접근 (Series 반환)
print("--- 컬럼 접근 ---")
print(df["이름"])              # 단일 컬럼
print()
print(df[["이름", "점수"]])    # 여러 컬럼 (DataFrame 반환)

# 행 접근 - loc (라벨 기반)
print("\n--- loc (라벨 기반) ---")
print(df.loc[0])              # 인덱스 0인 행
print()
print(df.loc[0:2])            # 인덱스 0~2 (끝 포함!)

# 행 접근 - iloc (위치 기반)
print("\n--- iloc (위치 기반) ---")
print(df.iloc[0])             # 첫 번째 행
print()
print(df.iloc[0:2])           # 첫 두 행 (끝 미포함!)

# 특정 셀 접근
print(f"\n특정 셀: {df.loc[0, '이름']}")      # 홍길동
print(f"특정 셀: {df.iloc[1, 3]}")             # 92

print()


# ============================================================
# 5. 조건부 필터링
# ============================================================
print("=== 조건부 필터링 ===")

# 점수가 90 이상인 사람
# JS: data.filter(d => d.점수 >= 90)  →  Python: df[df["점수"] >= 90]
high_scores = df[df["점수"] >= 90]
print("점수 90 이상:")
print(high_scores)

# 서울에 사는 사람
seoul = df[df["도시"] == "서울"]
print("\n서울 거주:")
print(seoul)

# 복합 조건 (& 사용, 각 조건을 괄호로!)
result = df[(df["점수"] >= 80) & (df["나이"] < 30)]
print("\n80점 이상 & 30세 미만:")
print(result)

# isin() 사용
big_cities = df[df["도시"].isin(["서울", "부산"])]
print("\n서울 또는 부산:")
print(big_cities)

print()


# ============================================================
# 6. 컬럼 추가/수정/삭제
# ============================================================
print("=== 컬럼 조작 ===")

df_copy = df.copy()

# 컬럼 추가
df_copy["등급"] = ["B", "A", "C", "A", "B"]
df_copy["보너스"] = df_copy["점수"] * 10

# 컬럼 수정
df_copy["나이"] = df_copy["나이"] + 1

# 컬럼 삭제
df_copy = df_copy.drop(columns=["보너스"])

print(df_copy)

print()


# ============================================================
# 7. 기본 통계
# ============================================================
print("=== 기본 통계 ===")

print(f"평균 점수: {df['점수'].mean():.1f}")
print(f"중앙값:    {df['점수'].median()}")
print(f"표준편차:  {df['점수'].std():.2f}")
print(f"최대:      {df['점수'].max()}")
print(f"최소:      {df['점수'].min()}")
print(f"합계:      {df['점수'].sum()}")

# value_counts: 고유값 개수
print(f"\n도시별 인원:\n{df['도시'].value_counts()}")

# 고유값
print(f"\n고유 도시: {df['도시'].unique()}")
print(f"도시 종류 수: {df['도시'].nunique()}")

print()


# ============================================================
# 8. 정렬
# ============================================================
print("=== 정렬 ===")

# 단일 컬럼 정렬
sorted_df = df.sort_values("점수", ascending=False)
print("점수 내림차순:")
print(sorted_df)

# 여러 컬럼 정렬
sorted_df2 = df.sort_values(["도시", "점수"], ascending=[True, False])
print("\n도시 오름차순 + 점수 내림차순:")
print(sorted_df2)

# 인덱스 재설정
sorted_df = sorted_df.reset_index(drop=True)
print("\n인덱스 재설정:")
print(sorted_df)

print()


# ============================================================
# 9. CSV 파일 읽기/쓰기
# ============================================================
print("=== CSV 읽기/쓰기 ===")

import os
os.makedirs("temp_data", exist_ok=True)

# CSV 저장
df.to_csv("temp_data/students.csv", index=False, encoding="utf-8-sig")
print("students.csv 저장 완료!")

# CSV 읽기
df_loaded = pd.read_csv("temp_data/students.csv")
print("\n불러온 데이터:")
print(df_loaded)

print()


# ============================================================
# 10. 실전 예제: 간단한 데이터 분석
# ============================================================
print("=== 실전 예제: 판매 데이터 분석 ===")

np.random.seed(42)
sales_data = {
    "날짜": pd.date_range("2025-01-01", periods=20, freq="D"),
    "상품": np.random.choice(["노트북", "태블릿", "스마트폰"], 20),
    "수량": np.random.randint(1, 10, 20),
    "단가": np.random.choice([1200000, 800000, 500000], 20)
}
sales = pd.DataFrame(sales_data)
sales["매출"] = sales["수량"] * sales["단가"]

print("판매 데이터 (처음 5행):")
print(sales.head())

print(f"\n총 매출: {sales['매출'].sum():,}원")
print(f"평균 매출: {sales['매출'].mean():,.0f}원")

print(f"\n상품별 매출 합계:")
print(sales.groupby("상품")["매출"].sum().sort_values(ascending=False))

print(f"\n상품별 판매 수량:")
print(sales.groupby("상품")["수량"].sum())


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] 5명의 학생 데이터(이름, 국어, 영어, 수학)로 DataFrame을 만들고
         각 과목의 평균과 학생별 총점을 구하세요.

[연습 2] DataFrame에서 총점 기준 상위 3명을 출력하세요.

[연습 3] CSV 파일을 읽어 특정 조건의 데이터만 필터링하여
         새 CSV로 저장하세요.
"""

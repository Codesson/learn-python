"""
Chapter 18: matplotlib 기초
==============================
데이터 시각화의 기본 라이브러리 matplotlib를 배웁니다.
실행 전: pip install matplotlib
"""

# ============================================================
# JavaScript 개발자를 위한 matplotlib 안내
# ============================================================
#
#  JS 차트 라이브러리와의 비교:
#  - Chart.js, D3.js, Plotly.js → matplotlib (정적 그래프)
#  - matplotlib는 서버 사이드에서 이미지 파일로 그래프를 생성합니다.
#  - 브라우저가 아닌 PNG/PDF 파일로 저장하는 것이 기본 사용법입니다.
#  - 인터랙티브가 필요하면 Plotly(Python)를 사용합니다.
#
#  개념 매핑:
#  - figure ≈ canvas 전체
#  - axes ≈ 개별 차트 영역
#  - plt.show() ≈ 화면에 렌더링
#  - plt.savefig() ≈ 이미지 파일로 내보내기
#

import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정 (macOS)
plt.rcParams["font.family"] = "AppleGothic"
# Windows: plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False  # 마이너스 부호 깨짐 방지


# ============================================================
# 1. 기본 선 그래프 (Line Plot)
# ============================================================
print("=== 1. 선 그래프 ===")

# 가장 간단한 그래프
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(8, 5))     # 그래프 크기 설정
plt.plot(x, y)
plt.title("기본 선 그래프")
plt.xlabel("X축")
plt.ylabel("Y축")
plt.savefig("temp_data/01_basic_line.png", dpi=100, bbox_inches="tight")
plt.close()
print("01_basic_line.png 저장!")

# 스타일 적용
x = np.linspace(0, 10, 100)   # 0~10 사이 100개 점

plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x), label="sin(x)", color="blue", linewidth=2)
plt.plot(x, np.cos(x), label="cos(x)", color="red", linestyle="--", linewidth=2)
plt.title("삼각함수 그래프", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.legend(fontsize=12)         # 범례
plt.grid(True, alpha=0.3)      # 격자
plt.axhline(y=0, color="gray", linestyle="-", linewidth=0.5)  # 가로선
plt.savefig("temp_data/02_styled_line.png", dpi=100, bbox_inches="tight")
plt.close()
print("02_styled_line.png 저장!")

print()


# ============================================================
# 2. 막대 그래프 (Bar Chart)
# ============================================================
print("=== 2. 막대 그래프 ===")

categories = ["Python", "JavaScript", "Java", "C++", "Go"]
values = [35, 25, 20, 10, 10]
colors = ["#3776AB", "#F7DF1E", "#ED8B00", "#00599C", "#00ADD8"]

plt.figure(figsize=(10, 6))
bars = plt.bar(categories, values, color=colors, edgecolor="white", linewidth=1.5)

# 막대 위에 값 표시
for bar, val in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
             f"{val}%", ha="center", va="bottom", fontsize=12, fontweight="bold")

plt.title("프로그래밍 언어 인기도", fontsize=16)
plt.ylabel("비율 (%)", fontsize=12)
plt.ylim(0, 40)
plt.savefig("temp_data/03_bar_chart.png", dpi=100, bbox_inches="tight")
plt.close()
print("03_bar_chart.png 저장!")

# 가로 막대 그래프
plt.figure(figsize=(10, 6))
plt.barh(categories, values, color=colors)
plt.title("프로그래밍 언어 인기도 (가로)", fontsize=16)
plt.xlabel("비율 (%)")
plt.savefig("temp_data/04_barh_chart.png", dpi=100, bbox_inches="tight")
plt.close()
print("04_barh_chart.png 저장!")

print()


# ============================================================
# 3. 산점도 (Scatter Plot)
# ============================================================
print("=== 3. 산점도 ===")

np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5
colors = np.random.rand(100)
sizes = np.abs(np.random.randn(100)) * 200

plt.figure(figsize=(10, 7))
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap="viridis", edgecolors="white")
plt.colorbar(scatter, label="색상 값")
plt.title("산점도 예제", fontsize=16)
plt.xlabel("X", fontsize=12)
plt.ylabel("Y", fontsize=12)
plt.grid(True, alpha=0.3)
plt.savefig("temp_data/05_scatter.png", dpi=100, bbox_inches="tight")
plt.close()
print("05_scatter.png 저장!")

print()


# ============================================================
# 4. 히스토그램 (Histogram)
# ============================================================
print("=== 4. 히스토그램 ===")

np.random.seed(42)
data = np.random.normal(170, 10, 1000)   # 평균 170, 표준편차 10

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color="steelblue", edgecolor="white", alpha=0.7)
plt.axvline(x=np.mean(data), color="red", linestyle="--", label=f"평균: {np.mean(data):.1f}")
plt.title("키 분포 (정규분포)", fontsize=16)
plt.xlabel("키 (cm)", fontsize=12)
plt.ylabel("빈도", fontsize=12)
plt.legend(fontsize=12)
plt.savefig("temp_data/06_histogram.png", dpi=100, bbox_inches="tight")
plt.close()
print("06_histogram.png 저장!")

print()


# ============================================================
# 5. 원형 그래프 (Pie Chart)
# ============================================================
print("=== 5. 원형 그래프 ===")

labels = ["Python", "JavaScript", "Java", "C++", "기타"]
sizes = [35, 25, 20, 10, 10]
explode = (0.05, 0, 0, 0, 0)   # Python 조각을 살짝 분리
colors = ["#3776AB", "#F7DF1E", "#ED8B00", "#00599C", "#AAAAAA"]

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=90,
        textprops={"fontsize": 12})
plt.title("프로그래밍 언어 점유율", fontsize=16)
plt.savefig("temp_data/07_pie_chart.png", dpi=100, bbox_inches="tight")
plt.close()
print("07_pie_chart.png 저장!")

print()


# ============================================================
# 6. 박스 플롯 (Box Plot)
# ============================================================
print("=== 6. 박스 플롯 ===")

np.random.seed(42)
data = [
    np.random.normal(75, 10, 50),    # 수학
    np.random.normal(80, 8, 50),     # 영어
    np.random.normal(70, 15, 50),    # 과학
    np.random.normal(85, 5, 50),     # 국어
]

plt.figure(figsize=(10, 6))
bp = plt.boxplot(data, labels=["수학", "영어", "과학", "국어"],
                 patch_artist=True)

colors = ["#FF9999", "#66B2FF", "#99FF99", "#FFCC99"]
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)

plt.title("과목별 성적 분포", fontsize=16)
plt.ylabel("점수", fontsize=12)
plt.grid(True, alpha=0.3, axis="y")
plt.savefig("temp_data/08_boxplot.png", dpi=100, bbox_inches="tight")
plt.close()
print("08_boxplot.png 저장!")

print()


# ============================================================
# 7. 그래프 꾸미기 옵션 정리
# ============================================================
print("=== 7. 스타일 옵션 정리 ===")

"""
[선 스타일]
  linestyle (ls): '-', '--', '-.', ':', 'None'
  linewidth (lw): 선 두께 (숫자)
  color (c): 색상 ('red', '#FF0000', (1,0,0), 'C0')

[마커]
  marker: 'o', 's', '^', 'D', 'v', '*', '+'
  markersize (ms): 마커 크기
  markerfacecolor (mfc): 마커 내부 색
  markeredgecolor (mec): 마커 테두리 색

[기타]
  alpha: 투명도 (0~1)
  label: 범례용 라벨
  zorder: 그리기 순서
"""

# 다양한 스타일 시연
x = np.linspace(0, 10, 20)

plt.figure(figsize=(12, 8))
plt.plot(x, np.sin(x), "ro-", label="원형 마커 + 실선", markersize=8)
plt.plot(x, np.sin(x + 1), "bs--", label="사각 마커 + 점선", markersize=6)
plt.plot(x, np.sin(x + 2), "g^-.", label="삼각 마커 + 점선", markersize=8)
plt.plot(x, np.sin(x + 3), "m*:", label="별 마커 + 점선", markersize=10)

plt.title("다양한 선/마커 스타일", fontsize=16)
plt.xlabel("X", fontsize=12)
plt.ylabel("Y", fontsize=12)
plt.legend(loc="upper right", fontsize=10)
plt.grid(True, alpha=0.3)
plt.savefig("temp_data/09_styles.png", dpi=100, bbox_inches="tight")
plt.close()
print("09_styles.png 저장!")

print()


# ============================================================
# 8. pandas와 함께 사용
# ============================================================
print("=== 8. pandas + matplotlib ===")
import pandas as pd

# 예제 데이터
months = ["1월", "2월", "3월", "4월", "5월", "6월"]
df = pd.DataFrame({
    "월": months,
    "매출": [1200, 1350, 1500, 1400, 1650, 1800],
    "비용": [800, 850, 900, 870, 950, 1000]
})

# pandas의 plot() 메서드 활용
fig, ax = plt.subplots(figsize=(10, 6))
df.plot(x="월", y=["매출", "비용"], kind="bar", ax=ax, color=["#4CAF50", "#FF5722"])
ax.set_title("월별 매출/비용", fontsize=16)
ax.set_ylabel("금액 (만원)", fontsize=12)
ax.set_xlabel("")
ax.legend(fontsize=12)

# 값 표시
for container in ax.containers:
    ax.bar_label(container, fontsize=9)

plt.tight_layout()
plt.savefig("temp_data/10_pandas_plot.png", dpi=100, bbox_inches="tight")
plt.close()
print("10_pandas_plot.png 저장!")

print("\n모든 그래프가 temp_data/ 폴더에 저장되었습니다!")
print("파일 탐색기에서 확인해 보세요.")


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] 1월~12월 기온 데이터를 선 그래프로 그려보세요.
         (적절한 타이틀, 축 라벨, 격자 추가)

[연습 2] 5개 카테고리의 데이터를 막대 그래프와 원형 그래프로
         각각 시각화하세요.

[연습 3] 두 변수의 상관관계를 산점도로 그리고,
         추세선을 추가해 보세요.
         (힌트: np.polyfit과 np.polyval 활용)
"""

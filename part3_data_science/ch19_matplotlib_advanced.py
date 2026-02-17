"""
Chapter 19: matplotlib 심화
==============================
서브플롯, 고급 스타일, 다양한 시각화 기법을 배웁니다.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

os.makedirs("temp_data", exist_ok=True)

plt.rcParams["font.family"] = "AppleGothic"
plt.rcParams["axes.unicode_minus"] = False


# ============================================================
# 1. 서브플롯 (Subplots)
# ============================================================
print("=== 1. 서브플롯 ===")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# (0,0) - 선 그래프
x = np.linspace(0, 10, 100)
axes[0, 0].plot(x, np.sin(x), color="blue")
axes[0, 0].set_title("선 그래프 (sin)")
axes[0, 0].grid(True, alpha=0.3)

# (0,1) - 막대 그래프
categories = ["A", "B", "C", "D", "E"]
values = [23, 45, 56, 78, 33]
axes[0, 1].bar(categories, values, color=["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"])
axes[0, 1].set_title("막대 그래프")

# (1,0) - 산점도
np.random.seed(42)
x = np.random.randn(50)
y = x + np.random.randn(50) * 0.5
axes[1, 0].scatter(x, y, alpha=0.7, c="purple", edgecolors="white")
axes[1, 0].set_title("산점도")

# (1,1) - 히스토그램
data = np.random.normal(0, 1, 1000)
axes[1, 1].hist(data, bins=30, color="orange", edgecolor="white", alpha=0.7)
axes[1, 1].set_title("히스토그램")

plt.suptitle("서브플롯 예제", fontsize=18, fontweight="bold")
plt.tight_layout()
plt.savefig("temp_data/11_subplots.png", dpi=100, bbox_inches="tight")
plt.close()
print("11_subplots.png 저장!")

print()


# ============================================================
# 2. 다양한 레이아웃
# ============================================================
print("=== 2. 다양한 레이아웃 ===")

# gridspec으로 비균일 레이아웃
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(12, 8))
gs = GridSpec(2, 3, figure=fig)

# 큰 그래프 (왼쪽 2/3)
ax1 = fig.add_subplot(gs[0, :2])
x = np.linspace(0, 10, 100)
ax1.plot(x, np.sin(x), "b-", linewidth=2)
ax1.plot(x, np.cos(x), "r--", linewidth=2)
ax1.set_title("메인 그래프")
ax1.legend(["sin(x)", "cos(x)"])
ax1.grid(True, alpha=0.3)

# 오른쪽 위
ax2 = fig.add_subplot(gs[0, 2])
ax2.bar(["A", "B", "C"], [30, 50, 20], color=["#FF6B6B", "#4ECDC4", "#45B7D1"])
ax2.set_title("서브 1")

# 왼쪽 아래
ax3 = fig.add_subplot(gs[1, 0])
np.random.seed(0)
ax3.hist(np.random.randn(500), bins=20, color="skyblue", edgecolor="white")
ax3.set_title("서브 2")

# 가운데 아래
ax4 = fig.add_subplot(gs[1, 1])
ax4.scatter(np.random.rand(30), np.random.rand(30), c="green", alpha=0.6)
ax4.set_title("서브 3")

# 오른쪽 아래
ax5 = fig.add_subplot(gs[1, 2])
sizes = [40, 30, 20, 10]
ax5.pie(sizes, labels=["A", "B", "C", "D"], autopct="%1.0f%%")
ax5.set_title("서브 4")

plt.suptitle("비균일 레이아웃", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig("temp_data/12_gridspec.png", dpi=100, bbox_inches="tight")
plt.close()
print("12_gridspec.png 저장!")

print()


# ============================================================
# 3. 이중 Y축
# ============================================================
print("=== 3. 이중 Y축 ===")

months = np.arange(1, 13)
temperature = [2, 4, 10, 16, 22, 27, 29, 28, 23, 16, 8, 3]
rainfall = [30, 40, 55, 80, 100, 150, 300, 280, 150, 60, 40, 25]

fig, ax1 = plt.subplots(figsize=(12, 6))

color1 = "#FF6B6B"
ax1.set_xlabel("월", fontsize=12)
ax1.set_ylabel("기온 (°C)", color=color1, fontsize=12)
ax1.plot(months, temperature, color=color1, marker="o", linewidth=2, label="기온")
ax1.tick_params(axis="y", labelcolor=color1)

ax2 = ax1.twinx()  # 두 번째 Y축
color2 = "#4ECDC4"
ax2.set_ylabel("강수량 (mm)", color=color2, fontsize=12)
ax2.bar(months, rainfall, color=color2, alpha=0.5, label="강수량")
ax2.tick_params(axis="y", labelcolor=color2)

plt.title("월별 기온 및 강수량", fontsize=16)
ax1.set_xticks(months)

# 범례 합치기
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

plt.savefig("temp_data/13_dual_axis.png", dpi=100, bbox_inches="tight")
plt.close()
print("13_dual_axis.png 저장!")

print()


# ============================================================
# 4. 히트맵 (Heatmap)
# ============================================================
print("=== 4. 히트맵 ===")

np.random.seed(42)
data = np.random.rand(5, 7)
days = ["월", "화", "수", "목", "금", "토", "일"]
weeks = ["1주", "2주", "3주", "4주", "5주"]

fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(data, cmap="YlOrRd", aspect="auto")

ax.set_xticks(range(len(days)))
ax.set_yticks(range(len(weeks)))
ax.set_xticklabels(days)
ax.set_yticklabels(weeks)

# 값 표시
for i in range(len(weeks)):
    for j in range(len(days)):
        text = ax.text(j, i, f"{data[i, j]:.2f}",
                       ha="center", va="center", fontsize=10,
                       color="white" if data[i, j] > 0.5 else "black")

plt.colorbar(im, label="활동량")
plt.title("주간 활동량 히트맵", fontsize=16)
plt.savefig("temp_data/14_heatmap.png", dpi=100, bbox_inches="tight")
plt.close()
print("14_heatmap.png 저장!")

print()


# ============================================================
# 5. 스타일 테마
# ============================================================
print("=== 5. 스타일 테마 ===")

# 사용 가능한 스타일 목록
print(f"사용 가능한 스타일: {plt.style.available[:10]}...")

# ggplot 스타일 적용 예시
with plt.style.context("ggplot"):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    x = np.linspace(0, 10, 50)
    axes[0].plot(x, np.sin(x), linewidth=2)
    axes[0].set_title("ggplot 스타일 - 선")

    axes[1].bar(["A", "B", "C", "D"], [20, 35, 30, 15])
    axes[1].set_title("ggplot 스타일 - 막대")

    axes[2].scatter(np.random.rand(50), np.random.rand(50), s=100, alpha=0.7)
    axes[2].set_title("ggplot 스타일 - 산점도")

    plt.suptitle("ggplot 스타일 테마", fontsize=16)
    plt.tight_layout()
    plt.savefig("temp_data/15_ggplot_style.png", dpi=100, bbox_inches="tight")
    plt.close()

print("15_ggplot_style.png 저장!")

print()


# ============================================================
# 6. 실전 예제: 대시보드
# ============================================================
print("=== 6. 실전 예제: 대시보드 ===")

np.random.seed(42)

# 데이터 생성
months = ["1월", "2월", "3월", "4월", "5월", "6월",
          "7월", "8월", "9월", "10월", "11월", "12월"]
revenue = [120, 135, 150, 140, 165, 180, 195, 210, 190, 175, 155, 200]
costs = [80, 85, 90, 87, 95, 100, 110, 120, 105, 95, 88, 108]
profit = [r - c for r, c in zip(revenue, costs)]

departments = ["영업", "개발", "마케팅", "인사", "경영"]
dept_budget = [350, 500, 200, 150, 300]

regions = ["서울", "경기", "부산", "대구", "기타"]
region_sales = [40, 25, 15, 10, 10]

fig = plt.figure(figsize=(16, 10))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.3)

# 1) 매출/비용 추이
ax1 = fig.add_subplot(gs[0, :2])
ax1.fill_between(range(12), revenue, alpha=0.3, color="#4CAF50")
ax1.plot(range(12), revenue, "o-", color="#4CAF50", linewidth=2, label="매출")
ax1.fill_between(range(12), costs, alpha=0.3, color="#FF5722")
ax1.plot(range(12), costs, "s--", color="#FF5722", linewidth=2, label="비용")
ax1.set_xticks(range(12))
ax1.set_xticklabels(months, fontsize=9)
ax1.set_ylabel("금액 (백만원)")
ax1.set_title("월별 매출/비용 추이", fontsize=14)
ax1.legend()
ax1.grid(True, alpha=0.3)

# 2) 지역별 비율
ax2 = fig.add_subplot(gs[0, 2])
colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#DDD"]
ax2.pie(region_sales, labels=regions, autopct="%1.0f%%", colors=colors, startangle=90)
ax2.set_title("지역별 매출 비율", fontsize=14)

# 3) 월별 영업이익
ax3 = fig.add_subplot(gs[1, :2])
bar_colors = ["#4CAF50" if p > 0 else "#FF5722" for p in profit]
ax3.bar(range(12), profit, color=bar_colors, edgecolor="white")
ax3.set_xticks(range(12))
ax3.set_xticklabels(months, fontsize=9)
ax3.set_ylabel("금액 (백만원)")
ax3.set_title("월별 영업이익", fontsize=14)
ax3.axhline(y=0, color="gray", linewidth=0.5)
ax3.grid(True, alpha=0.3, axis="y")

# 4) 부서별 예산
ax4 = fig.add_subplot(gs[1, 2])
bars = ax4.barh(departments, dept_budget, color=["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"])
for bar, val in zip(bars, dept_budget):
    ax4.text(val + 5, bar.get_y() + bar.get_height() / 2, f"{val}", va="center")
ax4.set_xlabel("예산 (백만원)")
ax4.set_title("부서별 예산", fontsize=14)

plt.suptitle("2025년 경영 대시보드", fontsize=18, fontweight="bold", y=1.02)
plt.savefig("temp_data/16_dashboard.png", dpi=150, bbox_inches="tight")
plt.close()
print("16_dashboard.png 저장!")

print("\n모든 고급 그래프가 temp_data/ 폴더에 저장되었습니다!")


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] 4개의 서브플롯으로 sin, cos, tan, exp 함수를
         각각 그려보세요.

[연습 2] 이중 Y축을 사용하여 주가(선)와 거래량(막대)을
         함께 시각화하세요.

[연습 3] 자신만의 대시보드를 만들어 보세요.
         (최소 4개의 서브플롯, 다양한 차트 타입)
"""

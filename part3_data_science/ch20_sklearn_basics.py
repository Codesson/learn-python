"""
Chapter 20: Scikit-learn 기초
================================
머신러닝 라이브러리 Scikit-learn의 기본을 배웁니다.
실행 전: pip install scikit-learn
"""

# ============================================================
# JavaScript 개발자를 위한 Scikit-learn 안내
# ============================================================
#
#  JS 생태계에는 Scikit-learn에 대응하는 라이브러리가 거의 없습니다.
#  (TensorFlow.js가 있지만 목적이 다릅니다)
#
#  Scikit-learn은 "전통적인 머신러닝"의 표준 도구입니다:
#  - 분류(Classification): 스팸 메일 판별, 이미지 분류
#  - 회귀(Regression): 집값 예측, 주가 예측
#  - 클러스터링(Clustering): 고객 세분화
#  - 전처리(Preprocessing): 데이터 정규화, 결측치 처리
#
#  핵심 패턴 (모든 모델이 동일!):
#    model = ModelClass()       # 모델 생성
#    model.fit(X_train, y_train) # 학습
#    predictions = model.predict(X_test)  # 예측
#
#  이 일관된 API가 Scikit-learn의 가장 큰 장점입니다.
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

plt.rcParams["font.family"] = "AppleGothic"
plt.rcParams["axes.unicode_minus"] = False
import os
os.makedirs("temp_data", exist_ok=True)


# ============================================================
# 1. 내장 데이터셋 살펴보기
# ============================================================
print("=== 1. 내장 데이터셋 ===")

# Iris 데이터셋 (꽃 분류)
iris = datasets.load_iris()

print(f"데이터 키: {list(iris.keys())}")
print(f"특성 이름: {iris.feature_names}")
print(f"타겟 이름: {iris.target_names}")
print(f"데이터 shape: {iris.data.shape}")   # (150, 4) = 150개 샘플, 4개 특성
print(f"타겟 shape: {iris.target.shape}")

# DataFrame으로 변환
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = [iris.target_names[t] for t in iris.target]
print(f"\n데이터 미리보기:")
print(df.head(10))
print(f"\n기술 통계:")
print(df.describe())

# 데이터 시각화
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
colors = ["red", "green", "blue"]
for i, species in enumerate(iris.target_names):
    mask = iris.target == i
    axes[0].scatter(iris.data[mask, 0], iris.data[mask, 1],
                    c=colors[i], label=species, alpha=0.7)
    axes[1].scatter(iris.data[mask, 2], iris.data[mask, 3],
                    c=colors[i], label=species, alpha=0.7)

axes[0].set_xlabel("꽃받침 길이")
axes[0].set_ylabel("꽃받침 너비")
axes[0].set_title("꽃받침 길이 vs 너비")
axes[0].legend()

axes[1].set_xlabel("꽃잎 길이")
axes[1].set_ylabel("꽃잎 너비")
axes[1].set_title("꽃잎 길이 vs 너비")
axes[1].legend()

plt.suptitle("Iris 데이터셋 시각화", fontsize=14)
plt.tight_layout()
plt.savefig("temp_data/17_iris_scatter.png", dpi=100, bbox_inches="tight")
plt.close()
print("\n17_iris_scatter.png 저장!")

print()


# ============================================================
# 2. 데이터 분할 (Train/Test Split)
# ============================================================
print("=== 2. Train/Test Split ===")

from sklearn.model_selection import train_test_split

X = iris.data       # 특성 (입력)
y = iris.target      # 타겟 (출력)

# 80% 학습, 20% 테스트
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"전체 데이터: {X.shape[0]}개")
print(f"학습 데이터: {X_train.shape[0]}개")
print(f"테스트 데이터: {X_test.shape[0]}개")

# stratify를 사용하면 클래스 비율이 유지됨
unique, counts = np.unique(y_train, return_counts=True)
print(f"\n학습 데이터 클래스 분포:")
for name, count in zip(iris.target_names, counts):
    print(f"  {name}: {count}개")

print()


# ============================================================
# 3. 데이터 전처리 - 스케일링
# ============================================================
print("=== 3. 데이터 스케일링 ===")

from sklearn.preprocessing import StandardScaler, MinMaxScaler

# StandardScaler: 평균 0, 표준편차 1
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # 학습 데이터로 fit + transform
X_test_scaled = scaler.transform(X_test)          # 테스트는 transform만!

print("스케일링 전:")
print(f"  평균: {X_train.mean(axis=0).round(2)}")
print(f"  표준편차: {X_train.std(axis=0).round(2)}")

print("StandardScaler 후:")
print(f"  평균: {X_train_scaled.mean(axis=0).round(2)}")
print(f"  표준편차: {X_train_scaled.std(axis=0).round(2)}")

# MinMaxScaler: 0~1 범위로
minmax = MinMaxScaler()
X_train_mm = minmax.fit_transform(X_train)
print("MinMaxScaler 후:")
print(f"  최소: {X_train_mm.min(axis=0)}")
print(f"  최대: {X_train_mm.max(axis=0)}")

print()


# ============================================================
# 4. 분류 모델 - KNN
# ============================================================
print("=== 4. KNN (K-최근접 이웃) ===")

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# 모델 생성 및 학습
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

# 예측
y_pred = knn.predict(X_test_scaled)

# 평가
accuracy = accuracy_score(y_test, y_pred)
print(f"정확도: {accuracy:.4f} ({accuracy * 100:.1f}%)")

print("\n분류 보고서:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 새 데이터 예측
new_flower = np.array([[5.0, 3.5, 1.5, 0.2]])
new_flower_scaled = scaler.transform(new_flower)
prediction = knn.predict(new_flower_scaled)
print(f"새 꽃 예측: {iris.target_names[prediction[0]]}")

print()


# ============================================================
# 5. 혼동 행렬 (Confusion Matrix)
# ============================================================
print("=== 5. 혼동 행렬 ===")

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_test, y_pred)
print(f"혼동 행렬:\n{cm}")

fig, ax = plt.subplots(figsize=(8, 6))
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                               display_labels=iris.target_names)
disp.plot(ax=ax, cmap="Blues")
plt.title("KNN 혼동 행렬", fontsize=14)
plt.savefig("temp_data/18_confusion_matrix.png", dpi=100, bbox_inches="tight")
plt.close()
print("18_confusion_matrix.png 저장!")

print()


# ============================================================
# 6. 다양한 분류 모델 비교
# ============================================================
print("=== 6. 모델 비교 ===")

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

models = {
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "로지스틱 회귀": LogisticRegression(max_iter=200),
    "결정 트리": DecisionTreeClassifier(random_state=42),
    "SVM": SVC(kernel="rbf"),
    "랜덤 포레스트": RandomForestClassifier(n_estimators=100, random_state=42),
}

results = {}
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc
    print(f"  {name:15s}: {acc:.4f}")

# 결과 시각화
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(results.keys(), results.values(),
              color=["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"],
              edgecolor="white", linewidth=1.5)
for bar, val in zip(bars, results.values()):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.005,
            f"{val:.2%}", ha="center", fontsize=11, fontweight="bold")
ax.set_ylim(0.8, 1.05)
ax.set_ylabel("정확도")
ax.set_title("분류 모델 성능 비교", fontsize=14)
ax.grid(True, alpha=0.3, axis="y")
plt.savefig("temp_data/19_model_comparison.png", dpi=100, bbox_inches="tight")
plt.close()
print("\n19_model_comparison.png 저장!")

print()


# ============================================================
# 7. 교차 검증 (Cross Validation)
# ============================================================
print("=== 7. 교차 검증 ===")

from sklearn.model_selection import cross_val_score

model = RandomForestClassifier(n_estimators=100, random_state=42)
scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")

print(f"5-Fold 교차 검증 결과:")
print(f"  각 폴드 점수: {scores.round(4)}")
print(f"  평균 정확도: {scores.mean():.4f} (+/- {scores.std():.4f})")

print()


# ============================================================
# 8. 간단한 회귀 예제
# ============================================================
print("=== 8. 선형 회귀 ===")

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 간단한 데이터 생성
np.random.seed(42)
X_reg = np.random.rand(100, 1) * 10      # 0~10 사이 값
y_reg = 2.5 * X_reg.ravel() + 5 + np.random.randn(100) * 2  # y = 2.5x + 5 + 노이즈

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

# 학습
reg = LinearRegression()
reg.fit(X_train_r, y_train_r)

# 예측
y_pred_r = reg.predict(X_test_r)

print(f"기울기: {reg.coef_[0]:.4f}")
print(f"절편: {reg.intercept_:.4f}")
print(f"MSE: {mean_squared_error(y_test_r, y_pred_r):.4f}")
print(f"R² 점수: {r2_score(y_test_r, y_pred_r):.4f}")

# 시각화
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(X_test_r, y_test_r, alpha=0.7, label="실제 값", color="blue")
ax.plot(X_test_r, y_pred_r, "r-", linewidth=2, label="예측 선")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title(f"선형 회귀 (y = {reg.coef_[0]:.2f}x + {reg.intercept_:.2f})")
ax.legend()
ax.grid(True, alpha=0.3)
plt.savefig("temp_data/20_linear_regression.png", dpi=100, bbox_inches="tight")
plt.close()
print("20_linear_regression.png 저장!")


# ============================================================
# 연습 문제
# ============================================================
"""
[연습 1] sklearn의 다른 내장 데이터셋(wine, digits 등)을
         불러와서 탐색해 보세요.

[연습 2] Iris 데이터에서 K값(1~20)을 변화시켜가며
         KNN의 정확도 변화를 그래프로 그려보세요.

[연습 3] Boston Housing 데이터(또는 California Housing)로
         집값을 예측하는 회귀 모델을 만들어 보세요.
"""

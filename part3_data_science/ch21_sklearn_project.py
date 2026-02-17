"""
Chapter 21: Scikit-learn 실전 프로젝트
========================================
전체 머신러닝 파이프라인을 경험합니다.
- 데이터 로딩 → 탐색 → 전처리 → 모델링 → 평가 → 개선
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import os
import warnings
warnings.filterwarnings("ignore")

plt.rcParams["font.family"] = "AppleGothic"
plt.rcParams["axes.unicode_minus"] = False
os.makedirs("temp_data", exist_ok=True)


print("=" * 60)
print("  프로젝트: 와인 품질 분류기 만들기")
print("=" * 60)


# ============================================================
# STEP 1: 데이터 로딩 & 탐색
# ============================================================
print("\n[STEP 1] 데이터 로딩 & 탐색")
print("-" * 40)

wine = datasets.load_wine()
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = pd.Series(wine.target, name="class")

print(f"샘플 수: {X.shape[0]}")
print(f"특성 수: {X.shape[1]}")
print(f"클래스: {wine.target_names}")

print(f"\n클래스 분포:")
for i, name in enumerate(wine.target_names):
    count = (y == i).sum()
    print(f"  {name}: {count}개 ({count/len(y)*100:.1f}%)")

print(f"\n기술 통계 (처음 5개 특성):")
print(X.iloc[:, :5].describe().round(2))


# ============================================================
# STEP 2: 데이터 시각화
# ============================================================
print(f"\n[STEP 2] 데이터 시각화")
print("-" * 40)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
features_to_plot = ["alcohol", "malic_acid", "flavanoids",
                    "color_intensity", "hue", "proline"]
colors = ["#FF6B6B", "#4ECDC4", "#45B7D1"]

for idx, (ax, feat) in enumerate(zip(axes.flat, features_to_plot)):
    for i, name in enumerate(wine.target_names):
        mask = y == i
        ax.hist(X.loc[mask, feat], bins=15, alpha=0.6,
                color=colors[i], label=name)
    ax.set_title(feat, fontsize=12)
    ax.legend(fontsize=8)

plt.suptitle("주요 특성별 클래스 분포", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig("temp_data/21_wine_features.png", dpi=100, bbox_inches="tight")
plt.close()
print("21_wine_features.png 저장!")


# ============================================================
# STEP 3: 데이터 전처리
# ============================================================
print(f"\n[STEP 3] 데이터 전처리")
print("-" * 40)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"학습 데이터: {X_train.shape[0]}개")
print(f"테스트 데이터: {X_test.shape[0]}개")

# 스케일링
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("스케일링 완료!")
print(f"  학습 데이터 평균: {X_train_scaled.mean(axis=0)[:3].round(3)}")
print(f"  학습 데이터 표준편차: {X_train_scaled.std(axis=0)[:3].round(3)}")


# ============================================================
# STEP 4: 다양한 모델 학습 & 비교
# ============================================================
print(f"\n[STEP 4] 모델 학습 & 비교")
print("-" * 40)

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score

models = {
    "로지스틱 회귀": LogisticRegression(max_iter=1000, random_state=42),
    "KNN (K=5)": KNeighborsClassifier(n_neighbors=5),
    "결정 트리": DecisionTreeClassifier(random_state=42),
    "SVM (RBF)": SVC(kernel="rbf", random_state=42),
    "랜덤 포레스트": RandomForestClassifier(n_estimators=100, random_state=42),
    "그래디언트 부스팅": GradientBoostingClassifier(n_estimators=100, random_state=42),
}

results = {}
for name, model in models.items():
    # 교차 검증
    cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
    # 학습 & 테스트
    model.fit(X_train_scaled, y_train)
    test_acc = accuracy_score(y_test, model.predict(X_test_scaled))

    results[name] = {
        "cv_mean": cv_scores.mean(),
        "cv_std": cv_scores.std(),
        "test_acc": test_acc
    }
    print(f"  {name:20s}  CV: {cv_scores.mean():.4f}(±{cv_scores.std():.4f})  Test: {test_acc:.4f}")

# 비교 시각화
fig, ax = plt.subplots(figsize=(12, 6))
names = list(results.keys())
cv_means = [r["cv_mean"] for r in results.values()]
cv_stds = [r["cv_std"] for r in results.values()]
test_accs = [r["test_acc"] for r in results.values()]

x_pos = np.arange(len(names))
width = 0.35
bars1 = ax.bar(x_pos - width/2, cv_means, width, label="CV 평균", color="#4ECDC4",
               yerr=cv_stds, capsize=5)
bars2 = ax.bar(x_pos + width/2, test_accs, width, label="테스트 정확도", color="#FF6B6B")

ax.set_ylabel("정확도")
ax.set_title("모델 성능 비교", fontsize=14)
ax.set_xticks(x_pos)
ax.set_xticklabels(names, rotation=30, ha="right", fontsize=9)
ax.legend()
ax.set_ylim(0.8, 1.05)
ax.grid(True, alpha=0.3, axis="y")
plt.tight_layout()
plt.savefig("temp_data/22_model_comparison.png", dpi=100, bbox_inches="tight")
plt.close()
print("\n22_model_comparison.png 저장!")


# ============================================================
# STEP 5: 최적 모델 상세 평가
# ============================================================
print(f"\n[STEP 5] 최적 모델 상세 평가")
print("-" * 40)

# 가장 좋은 모델 선택
best_name = max(results, key=lambda k: results[k]["test_acc"])
print(f"최적 모델: {best_name}")

best_model = models[best_name]
y_pred = best_model.predict(X_test_scaled)

print(f"\n분류 보고서:")
print(classification_report(y_test, y_pred, target_names=wine.target_names))

# 혼동 행렬
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

fig, ax = plt.subplots(figsize=(8, 6))
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=wine.target_names)
disp.plot(ax=ax, cmap="Blues")
plt.title(f"{best_name} - 혼동 행렬", fontsize=14)
plt.savefig("temp_data/23_best_confusion.png", dpi=100, bbox_inches="tight")
plt.close()
print("23_best_confusion.png 저장!")


# ============================================================
# STEP 6: 하이퍼파라미터 튜닝
# ============================================================
print(f"\n[STEP 6] 하이퍼파라미터 튜닝")
print("-" * 40)

from sklearn.model_selection import GridSearchCV

# 랜덤 포레스트 파라미터 탐색
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 5, 10, 20],
    "min_samples_split": [2, 5, 10],
}

rf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(
    rf, param_grid, cv=5, scoring="accuracy", n_jobs=-1, verbose=0
)
grid_search.fit(X_train_scaled, y_train)

print(f"최적 파라미터: {grid_search.best_params_}")
print(f"최적 CV 점수: {grid_search.best_score_:.4f}")

# 최적 모델로 테스트
best_rf = grid_search.best_estimator_
y_pred_tuned = best_rf.predict(X_test_scaled)
tuned_acc = accuracy_score(y_test, y_pred_tuned)
print(f"튜닝 후 테스트 정확도: {tuned_acc:.4f}")


# ============================================================
# STEP 7: 특성 중요도
# ============================================================
print(f"\n[STEP 7] 특성 중요도 분석")
print("-" * 40)

importances = best_rf.feature_importances_
feature_imp = pd.Series(importances, index=wine.feature_names).sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(10, 7))
feature_imp.plot(kind="barh", color="#4ECDC4", edgecolor="white", ax=ax)
ax.set_xlabel("중요도")
ax.set_title("랜덤 포레스트 - 특성 중요도", fontsize=14)
ax.grid(True, alpha=0.3, axis="x")
plt.tight_layout()
plt.savefig("temp_data/24_feature_importance.png", dpi=100, bbox_inches="tight")
plt.close()
print("24_feature_importance.png 저장!")

print("\n상위 5개 중요 특성:")
for name, imp in feature_imp.iloc[-5:][::-1].items():
    print(f"  {name}: {imp:.4f}")


# ============================================================
# STEP 8: 파이프라인
# ============================================================
print(f"\n[STEP 8] 파이프라인")
print("-" * 40)

from sklearn.pipeline import Pipeline

# 전처리 + 모델을 하나로 묶기
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", RandomForestClassifier(
        **grid_search.best_params_, random_state=42
    ))
])

# 파이프라인으로 학습 (원본 데이터 사용 가능)
pipeline.fit(X_train, y_train)
pipe_acc = pipeline.score(X_test, y_test)
print(f"파이프라인 정확도: {pipe_acc:.4f}")

# 새 데이터 예측 (전처리 자동 적용!)
new_wine = X_test.iloc[:3]
predictions = pipeline.predict(new_wine)
print(f"\n새 와인 예측:")
for i, (idx, row) in enumerate(new_wine.iterrows()):
    actual = wine.target_names[y_test.iloc[i]]
    predicted = wine.target_names[predictions[i]]
    status = "O" if actual == predicted else "X"
    print(f"  [{status}] 실제: {actual}, 예측: {predicted}")


# ============================================================
# 최종 요약
# ============================================================
print("\n" + "=" * 60)
print("  프로젝트 요약")
print("=" * 60)
print(f"""
1. 데이터: Wine 데이터셋 ({X.shape[0]}개 샘플, {X.shape[1]}개 특성)
2. 전처리: StandardScaler로 정규화
3. 비교 모델: {len(models)}개 모델 비교
4. 최적 모델: {best_name}
5. 하이퍼파라미터 튜닝: GridSearchCV
6. 최종 정확도: {tuned_acc:.1%}
7. 가장 중요한 특성: {feature_imp.index[-1]}

학습 과정:
  데이터 로딩 → 탐색/시각화 → 전처리 → 모델 학습 →
  성능 평가 → 하이퍼파라미터 튜닝 → 특성 분석 → 파이프라인
""")

print("축하합니다! 머신러닝 프로젝트를 완료했습니다!")
print("temp_data/ 폴더에서 생성된 그래프를 확인하세요.")


# ============================================================
# 연습 문제 (최종 프로젝트)
# ============================================================
"""
[최종 프로젝트 1] digits 데이터셋으로 손글씨 숫자 분류기를 만드세요.
   - 데이터 탐색 및 시각화
   - 최소 3개 모델 비교
   - 혼동 행렬로 어떤 숫자를 자주 헷갈리는지 분석

[최종 프로젝트 2] California Housing 데이터셋으로 집값 예측 모델을 만드세요.
   - from sklearn.datasets import fetch_california_housing
   - 회귀 모델 사용 (LinearRegression, RandomForestRegressor 등)
   - MSE, R² 점수로 평가

[최종 프로젝트 3] 자신만의 데이터셋을 만들거나 찾아서
   전체 ML 파이프라인을 구축해 보세요.
   - Kaggle (https://www.kaggle.com) 에서 데이터셋 탐색
"""

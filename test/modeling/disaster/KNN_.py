from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
# 폰트 경로 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_prop = fm.FontProperties(fname=font_path, size=12)
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['axes.unicode_minus'] = False


# 데이터 준비
file_path = 'C:/Users/Administrator/Documents/conda/test/modeling/disaster/natural.csv'
dataset = pd.read_csv(file_path, encoding='euc-kr')

# 데이터 전처리
datas = dataset.copy()
datas = datas.drop(columns=['시작시간', '종료기간', '데이터기준일자'])

# 클래스 라벨 정의 및 인코딩
le_disaster = LabelEncoder()
datas['재해구분'] = le_disaster.fit_transform(datas['재해구분'])

# 데이터 분리
X = datas.drop(columns=['재해구분'])
y = datas['재해구분']

# 이상치 제거
from scipy import stats
z_scores = stats.zscore(X)
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
X_clean = X[filtered_entries]
y_clean = y[filtered_entries]

X_train, X_test, y_train, y_test = train_test_split(X_clean, y_clean, test_size=0.3, random_state=42)

# 스케일링
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# KNN 모델 훈련 (클래스 예측)
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train_scaled, y_train)

# 예측 수행
y_pred = knn_model.predict(X_test_scaled)

# 시각화
feature_names = ['순간최대풍속', '일최대강우량(mm)']  # 시각화할 피처
feature_indices = [X.columns.get_loc(name) for name in feature_names]
X_test_reduced = X_test_scaled[:, feature_indices]

x1 = np.linspace(X_test_reduced[:, 0].min(), X_test_reduced[:, 0].max(), 100)
x2 = np.linspace(X_test_reduced[:, 1].min(), X_test_reduced[:, 1].max(), 100)

X1, X2 = np.meshgrid(x1, x2)
X_grid_reduced = np.vstack([X1.ravel(), X2.ravel()]).T

# 나머지 피처는 평균값으로 설정
mean_values = X_train_scaled.mean(axis=0)
X_grid_full = np.hstack([X_grid_reduced, np.tile(mean_values[2:], (X_grid_reduced.shape[0], 1))])

# KNN 예측 수행
y_pred_grid = knn_model.predict(X_grid_full)
y_pred_grid = y_pred_grid.reshape(X1.shape)

# 시각화
plt.figure(figsize=(12, 8))
plt.contourf(X1, X2, y_pred_grid, alpha=0.3, cmap='coolwarm')
plt.scatter(X_test_reduced[:, 0], X_test_reduced[:, 1], c=y_test, edgecolor='k', cmap='coolwarm')
plt.colorbar(label='Predicted Class')
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.title('KNN Classification Visualization')
plt.show()
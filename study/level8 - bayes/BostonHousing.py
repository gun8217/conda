from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

import numpy as np
import pandas as pd


# 데이터 준비
file_path = 'C:/Users/Administrator/Documents/conda/study/level8 - bayes/BostonHousing.csv'
boston = pd.read_csv(file_path, index_col=0)
print(boston.head(),'\n', boston.tail(), boston.shape)


# # 결측치 제거 방법1 : 선택 행 삭제
# data = pd.read_csv(file_path)
# # data.info()
# # print(data.isnull().sum())
# print(data.columns[data.isnull().any()])
# data = data.dropna()
# print(data.shape)

# # 결측치 제거 방법2 : 평균으로 채우기
# mean_values = data.mean()
# filled_data = data.fillna(mean_values)

# # 결측치 제거 방법3 : 적절한 값으로 대체
# interpolated_data = data.interpolate()


X = boston[boston.columns[:-1]]
y = boston[boston.columns[-1]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 모델 초기화
regressor = DecisionTreeRegressor(random_state=42)

# 모델 훈련
regressor.fit(X_train, y_train)

# 모델 평가
train_acc = regressor.score(X_train, y_train)
print("훈련 정확도 :", train_acc)

pred = regressor.predict(X_test) # 모델 테스트

test_acc = regressor.score(X_test, y_test)
print("테스트 정확도 :", test_acc)

mse = mean_squared_error(y_test, pred)
print(f"Target 값의 최소값: {y_test.min()}, 최대값: {y_test.max()}")
print(f"Target의 성능 평가: {mse}")
print()


print(regressor.criterion)
print(regressor.feature_names_in_)
feature_importances_rounded = [round(imp, 4) for imp in regressor.feature_importances_]
print(feature_importances_rounded)
print()


# # 결정계수 계산
# y_mean = np.mean(y_test)
# ss_total = np.sum((y_test - y_mean) ** 2)  # 총 제곱합
# ss_residual = np.sum((y_test - pred) ** 2)  # 잔차 제곱합

# r2 = 1 - (ss_residual / ss_total)
# print(r2)

# 결정 계수 계산
re_score1 = regressor.score(X_test, y_test)
print(f"{re_score1 = }")
pred_r2 = regressor.predict(X_test)
r2_score2 = 1 - (np.sum(np.square(y_test - pred_r2))) / np.sum(np.square((y_test - np.mean(y_test))))
print(f"{r2_score2 = }")
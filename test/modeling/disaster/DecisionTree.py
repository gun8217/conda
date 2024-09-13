import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 데이터 준비
file_path = 'C:/Users/Administrator/Documents/conda/test/modeling/disaster/natural.csv'
dataset = pd.read_csv(file_path, encoding='euc-kr')

# 데이터 전처리
datas = dataset.copy()
datas = datas.drop(columns=['시작시간', '종료기간', '데이터기준일자'])

# 레이블 인코딩
le_disaster = LabelEncoder()
datas['재해구분'] = le_disaster.fit_transform(datas['재해구분'])

# 모델 훈련
X = datas.drop(columns=['중심기압(hPa)'])  # '중심기압(hPa)'은 제외
y = datas[['중심기압(hPa)']]

# 이상치 제거
from scipy import stats
z_scores = stats.zscore(X)
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
X_clean = X[filtered_entries]
y_clean = y[filtered_entries]

X_train, X_test, y_train, y_test = train_test_split(X_clean, y_clean,
                                                    test_size=0.3,
                                                    random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Decision Tree 모델 훈련
dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train_scaled, y_train)

# 모델 평가
train_acc = dt_model.score(X_train_scaled, y_train)
print("훈련 정확도 :", train_acc)

pred = dt_model.predict(X_test_scaled)  # 모델 테스트

test_acc = dt_model.score(X_test_scaled, y_test)
print("테스트 정확도 :", test_acc)

# Mean Squared Error 계산
y_test = y_test.values

mse = mean_squared_error(y_test, pred)
print(f"평균 제곱 오차 (MSE): {mse}")

squared_errors = (y_test - pred) ** 2
print("최소:", np.min(squared_errors))
print("최대:", np.max(squared_errors))

# R² Score 계산
r2 = r2_score(y_test, pred)
print(f"R² Score: {r2}")

# 새로운 데이터 준비
new_data = pd.DataFrame([{
    '중심기압(hPa)': 1005  # 예시로 설정한 새로운 중심기압 값
}], columns=['중심기압(hPa)'])

# 나머지 특성들을 평균값으로 대체
mean_values = X_train.mean()
for col in X.columns:
    if col != '중심기압(hPa)':
        new_data[col] = mean_values[col]

# '중심기압(hPa)'을 제외하고 스케일링
new_data_for_scaling = new_data.drop(columns=['중심기압(hPa)'])
new_data_scaled = scaler.transform(new_data_for_scaling)

# Decision Tree 모델을 사용하여 예측
prediction = dt_model.predict(new_data_scaled)
print("새로운 데이터에 대한 예측:", prediction)

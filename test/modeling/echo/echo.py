import numpy as np
import pandas as pd

# 데이터 준비
file_weather = 'test/modeling/echo/weather.csv'
weather = pd.read_csv(file_weather)
weather = weather[:-1]
file_energy = 'test/modeling/echo/energy.csv'
energy = pd.read_csv(file_energy, encoding='euc-kr')
energy['일시'] = energy['구분']

weather_df = weather[['일시', '평균기온(℃)', '평균최고기온(℃)', '최고기온(℃)', '평균최저기온(℃)', '최저기온(℃)']]
weather_df.loc[:, '일시'] = pd.to_datetime(weather_df['일시'], format='%y-%b').dt.strftime('%y.%m')
energy_df = energy[['일시', '전기(kw)', '가스(Nm3)', '수도(m3)']]
energy_df.loc[:, '일시'] = pd.to_datetime(energy_df['일시'], format='%Y-%m').dt.strftime('%y.%m')

merged_df = pd.merge(weather_df, energy_df, on='일시', how='left')

# merged_df.info()
# print(merged_df.isnull().sum())
# print(merged_df.columns[merged_df.isnull().any()])
training_df = merged_df.dropna() 
# print(training_df)

# # 중복 데이터 확인 및 제거
training_df.duplicated().sum()
# training_df.drop_duplicates(inplace=True)

# import seaborn as sns
# import matplotlib.pyplot as plt
# training_df.hist(bins=50, figsize=(20,15))
# plt.show()

# # 상관관계
# corr_mat = training_df.corr()
# print(corr_mat)

# # 왜도 확인
# print(training_df.skew())

from sklearn.model_selection import train_test_split
X = training_df[['평균기온(℃)', '평균최고기온(℃)', '최고기온(℃)', '평균최저기온(℃)', '최저기온(℃)']]
y = training_df['전기(kw)']

# 이상치 제거
from scipy import stats
z_scores = stats.zscore(X)
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
X_clean = X[filtered_entries]
y_clean = y[filtered_entries]

X_train, X_test, y_train, y_test = train_test_split(X_clean, y_clean, test_size=0.6, random_state=42)

# # 데이터 스케일링
# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# 모델 훈련
from sklearn.metrics import mean_squared_error, r2_score

# # Decision Tree Regressor
# from sklearn.tree import DecisionTreeRegressor
# decision_tree_model = DecisionTreeRegressor(random_state=42)
# decision_tree_model.fit(X_train, y_train)
# # 모델 평가
# train_acc = decision_tree_model.score(X_train, y_train)
# print("훈련 정확도 :", train_acc)
# decision_tree_pred = decision_tree_model.predict(X_test) # 모델 테스트
# print(decision_tree_pred)
# test_acc = decision_tree_model.score(X_test, y_test)
# print("테스트 정확도 :", test_acc)
# # Mean Squared Error 계산
# mse = mean_squared_error(y_test, decision_tree_pred)
# print(f"Mean Squared Error (MSE): {mse}")
# # R² Score 계산
# r2 = r2_score(y_test, decision_tree_pred)
# print(f"R² Score: {r2}\n")

# # RandomForest
# from sklearn.ensemble import RandomForestRegressor
# rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
# rf_model.fit(X_train, y_train)
# # 모델 평가
# train_acc = rf_model.score(X_train, y_train)
# print("훈련 정확도 :", train_acc)
# rf_pred = rf_model.predict(X_test) # 모델 테스트
# print(rf_pred)
# test_acc = rf_model.score(X_test, y_test)
# print("테스트 정확도 :", test_acc)
# # Mean Squared Error 계산
# mse = mean_squared_error(y_test, rf_pred)
# print(f"Mean Squared Error (MSE): {mse}")
# # R² Score 계산
# r2 = r2_score(y_test, rf_pred)
# print(f"R² Score: {r2}\n")

# # GradientBoostingRegressor
# from sklearn.ensemble import GradientBoostingRegressor
# gbm_model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
# gbm_model.fit(X_train, y_train)
# # 모델 평가
# train_acc = gbm_model.score(X_train, y_train)
# print("훈련 정확도 :", train_acc)
# gbm_pred = gbm_model.predict(X_test) # 모델 테스트
# print(gbm_pred)
# test_acc = gbm_model.score(X_test, y_test)
# print("테스트 정확도 :", test_acc)
# # Mean Squared Error 계산
# mse = mean_squared_error(y_test, gbm_pred)
# print(f"Mean Squared Error (MSE): {mse}")
# # R² Score 계산
# r2 = r2_score(y_test, gbm_pred)
# print(f"R² Score: {r2}\n")

# Lasso
from sklearn.linear_model import Lasso
lasso_model = Lasso(alpha=0.1)  # alpha 값 조정 가능
lasso_model.fit(X_train, y_train)
# 모델 평가
train_acc = lasso_model.score(X_train, y_train)
print("훈련 정확도 :", train_acc)
lasso_pred = lasso_model.predict(X_test) # 모델 테스트
print(lasso_pred)
test_acc = lasso_model.score(X_test, y_test)
print("테스트 정확도 :", test_acc)
# Mean Squared Error 계산
mse = mean_squared_error(y_test, lasso_pred)
print(f"Mean Squared Error (MSE): {mse}")
# R² Score 계산
r2 = r2_score(y_test, lasso_pred)
print(f"R² Score: {r2}\n")

# # Ridge
# from sklearn.linear_model import Ridge
# ridge_model = Ridge(alpha=1.0)  # alpha 값 조정 가능
# ridge_model.fit(X_train, y_train)
# # 모델 평가
# train_acc = ridge_model.score(X_train, y_train)
# print("훈련 정확도 :", train_acc)
# ridge_pred = ridge_model.predict(X_test) # 모델 테스트
# print(ridge_pred)
# test_acc = ridge_model.score(X_test, y_test)
# print("테스트 정확도 :", test_acc)
# # Mean Squared Error 계산
# mse = mean_squared_error(y_test, ridge_pred)
# print(f"Mean Squared Error (MSE): {mse}")
# # R² Score 계산
# r2 = r2_score(y_test, ridge_pred)
# print(f"R² Score: {r2}\n")


# NaN 값이 있는 행만 분리
missing_data = merged_df[merged_df['전기(kw)'].isna()]
X_missing = missing_data[['평균기온(℃)', '평균최고기온(℃)', '최고기온(℃)', '평균최저기온(℃)', '최저기온(℃)']]


# # Gradient Boosting 모델 생성 및 학습
# from sklearn.ensemble import GradientBoostingRegressor
# gbr_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
# gbr_model.fit(X, y)
# # 예측
# predicted_values = gbr_model.predict(X_missing)


# NaN 값을 채우거나 삭제하는 방식으로 데이터 준비
# NaN 값을 채우기 위해 SimpleImputer 사용
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
X_missing_imputed = imputer.fit_transform(X_missing)

# X_missing_imputed를 DataFrame으로 변환하고 피처 이름을 설정
X_missing_imputed_df = pd.DataFrame(X_missing_imputed, columns=['평균기온(℃)', '평균최고기온(℃)', '최고기온(℃)', '평균최저기온(℃)', '최저기온(℃)'])

# 예측 수행
predicted_values = lasso_model.predict(X_missing_imputed_df)

# 예측 결과를 원본 데이터에 업데이트
merged_df.loc[merged_df['전기(kw)'].isna(), '전기(kw)'] = predicted_values
# for i, column in enumerate(y.columns):
#     merged_df.loc[merged_df[column].isna(), column] = predicted_values[:, i]
# print(merged_df.head(),'\n', merged_df.tail(), merged_df.shape)

energy_all = merged_df[['일시', '전기(kw)']]
energy_all.loc[:, '전기(kw)'] = energy_all['전기(kw)'].astype(int)

# CSV 파일로 저장
file_merge = 'C:/Users/user/Documents/conda/test/modeling/echo/energy_all.csv'
energy_all.to_csv(file_merge, index=False, encoding='utf-8-sig')


import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
# 폰트 경로 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_prop = fm.FontProperties(fname=font_path, size=12)
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# 일시를 datetime 형식으로 변환
merged_df['일시'] = pd.to_datetime(merged_df['일시'], format='%y.%m')

# 데이터 정렬 (시간 순서대로)
merged_df = merged_df.sort_values(by='일시')

# 첫 번째 그래프 (보간 전)
plt.figure(figsize=(12, 10))

# 첫 번째 서브플롯 - 보간 전
plt.subplot(2, 1, 1)  # (행, 열, 순서)
plt.plot(merged_df['일시'], merged_df['전기(kw)'], marker='o')
plt.xlabel('일시')
plt.ylabel('전기(kw)')
plt.title('보간 전 전기 사용량')
plt.grid(alpha=0.5)

# # 두 번째 서브플롯 - 보간 후
# merged_df.set_index('일시', inplace=True)
# interpolated_power = merged_df[['전기(kw)']].interpolate()
# merged_df['전기(kw)'] = interpolated_power

# plt.subplot(2, 1, 2)  # (행, 열, 순서)
# plt.plot(merged_df.index, merged_df['전기(kw)'], marker='o')
# plt.xlabel('일시')
# plt.ylabel('전기(kw)')
# plt.title('보간 후 전기 사용량')
# plt.grid(alpha=0.5)

# 레이아웃 조정
plt.tight_layout()
plt.show()
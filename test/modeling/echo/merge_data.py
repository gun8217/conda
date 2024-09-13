import pandas as pd

# 데이터 준비
file_weather = 'C:/Users/Administrator/Documents/conda/test/modeling/echo/weather.csv'
weather = pd.read_csv(file_weather)
weather = weather[:-1]
file_energy = 'C:/Users/Administrator/Documents/conda/test/modeling/echo/energy.csv'
energy = pd.read_csv(file_energy, encoding='euc-kr')
energy['일시'] = energy['구분']

weather_df = weather[['일시', '평균기온(℃)', '평균최고기온(℃)', '최고기온(℃)', '평균최저기온(℃)', '최저기온(℃)']]
weather_df.loc[:, '일시'] = pd.to_datetime(weather_df['일시'], format='%y-%b').dt.strftime('%y.%m')
energy_df = energy[['일시', '전기(kw)', '가스(Nm3)', '수도(m3)']]
energy_df.loc[:, '일시'] = pd.to_datetime(energy_df['일시'], format='%Y-%m').dt.strftime('%y.%m')

merged_df = pd.merge(weather_df, energy_df, on='일시', how='left')

# 모델 훈련에 필요한 data만 추출
training_df = merged_df.dropna()

# 모델 훈련
from sklearn.model_selection import train_test_split
X = training_df[['평균기온(℃)', '평균최고기온(℃)', '최고기온(℃)', '평균최저기온(℃)', '최저기온(℃)']]
y = training_df['전기(kw)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree Regressor 모델 훈련
from sklearn.tree import DecisionTreeRegressor
decision_tree_model = DecisionTreeRegressor(random_state=42)
decision_tree_model.fit(X_train, y_train)

# RandomForest 모델 생성 및 학습
from sklearn.ensemble import RandomForestRegressor
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Gradient Boosting 모델 생성 및 학습
from sklearn.ensemble import GradientBoostingRegressor
gbr_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
gbr_model.fit(X_train, y_train)

# 예측
decision_tree_predictions = decision_tree_model.predict(X_test)
rf_predictions = rf_model.predict(X_test)
gbr_predictions = gbr_model.predict(X_test)



# NaN 값이 있는 행만 분리
missing_data = merged_df[merged_df['전기(kw)'].isna()]
X_missing = missing_data[['평균기온(℃)', '평균최고기온(℃)', '최고기온(℃)', '평균최저기온(℃)', '최저기온(℃)']]

# NaN 값을 채우기 위해 SimpleImputer 사용
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='median')
X_missing_imputed = imputer.fit_transform(X_missing)

# X_missing_imputed를 DataFrame으로 변환하고 피처 이름을 설정
X_missing_imputed_df = pd.DataFrame(X_missing_imputed, columns=['평균기온(℃)', '평균최고기온(℃)', '최고기온(℃)', '평균최저기온(℃)', '최저기온(℃)'])

# 예측 수행
predicted_values = decision_tree_model.predict(X_missing_imputed_df)

# 예측 결과를 원본 데이터에 업데이트
merged_df.loc[merged_df['전기(kw)'].isna(), '전기(kw)'] = predicted_values

energy_all = merged_df[['일시', '전기(kw)']]
energy_all.loc[:, '전기(kw)'] = energy_all['전기(kw)'].astype(int)

# CSV 파일로 저장
file_merge = 'C:/Users/Administrator/Documents/conda/test/modeling/echo/energy_all.csv'
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

# 그래프 그리기
plt.figure(figsize=(12, 6))
plt.plot(merged_df['일시'], merged_df['전기(kw)'], marker='o')
plt.xlabel('일시')
plt.ylabel('전기(kw)')
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()
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

# merged_df.info()
# print(merged_df.isnull().sum())
# print(merged_df.columns[merged_df.isnull().any()])
training_df = merged_df.dropna()
# print(training_df)


from sklearn.model_selection import train_test_split
X = training_df[['평균기온(℃)', '평균최고기온(℃)', '최고기온(℃)', '평균최저기온(℃)', '최저기온(℃)']]
y = training_df[['전기(kw)', '가스(Nm3)', '수도(m3)']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)


# NaN 값이 있는 행만 분리
missing_data = merged_df[merged_df['전기(kw)'].isna()]
X_missing = missing_data[['평균기온(℃)', '평균최고기온(℃)', '최고기온(℃)', '평균최저기온(℃)', '최저기온(℃)']]

# NaN 값을 채우거나 삭제하는 방식으로 데이터 준비
# NaN 값을 채우기 위해 SimpleImputer 사용
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
X_missing_imputed = imputer.fit_transform(X_missing)

# 예측 수행
predicted_values = model.predict(X_missing_imputed)

# 예측 결과를 원본 데이터에 업데이트
for i, column in enumerate(y.columns):
    merged_df.loc[merged_df[column].isna(), column] = predicted_values[:, i]
# print(merged_df.head(),'\n', merged_df.tail(), merged_df.shape)

energy_all = merged_df[['일시', '전기(kw)', '가스(Nm3)', '수도(m3)']]
energy_all.loc[:, ['전기(kw)', '가스(Nm3)', '수도(m3)']] = energy_all[['전기(kw)', '가스(Nm3)', '수도(m3)']].astype(int)

# CSV 파일로 저장
file_merge = 'C:/Users/Administrator/Documents/conda/test/modeling/echo/energy_all.csv'
energy_all.to_csv(file_merge, index=False, encoding='utf-8-sig')
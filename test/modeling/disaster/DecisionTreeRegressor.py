from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd

# 데이터 준비
# C:\Users\user\Documents\conda\test\modeling\natural.csv
file_path = 'C:/Users/user/Documents/conda/test/modeling/natural.csv'
dataset = pd.read_csv(file_path, encoding='euc-kr')
# print(dataset.head())

# 데이터 전처리
datas = dataset.copy()
datas = datas.drop(columns=['시작시간', '종료기간', '데이터기준일자'])
print(datas.head())

# '재해구분'을 숫자형으로 변환
le_disaster = LabelEncoder()
datas['재해구분'] = le_disaster.fit_transform(datas['재해구분'])

X = datas.drop(columns=['중심기압(hPa)'])
y = datas['중심기압(hPa)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 데이터 스케일링
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 하이퍼파라미터 조정 예시
param_grid = {
    'max_depth': [10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(DecisionTreeRegressor(random_state=42), param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train_scaled, y_train)

# 최적 하이퍼파라미터로 모델 재훈련
best_regressor = grid_search.best_estimator_
best_regressor.fit(X_train_scaled, y_train)

# 모델 평가
train_acc = best_regressor.score(X_train_scaled, y_train)
test_acc = best_regressor.score(X_test_scaled, y_test)
pred = best_regressor.predict(X_test_scaled)
mse = mean_squared_error(y_test, pred)
mae = mean_absolute_error(y_test, pred)
r2 = r2_score(y_test, pred)

print(f"훈련 정확도: {train_acc}")
print(f"테스트 정확도: {test_acc}")
print(f"Target 값의 최소값: {y_test.min()}, 최대값: {y_test.max()}")
print(f"Target의 MSE: {mse}")
print(f"Target의 MAE: {mae}")
print(f"R^2 Score: {r2}")
print()

# 예측할 중심기압 값
new_pressure_value = 1005  # 예를 들어 1005 hPa

# X.columns에서 필요한 모든 열을 포함하여 기본값으로 데이터프레임 생성
new_pressure_df = pd.DataFrame([{
    '재해구분': 0,       # 기본값 또는 적절한 값
    '기온': 0,          # 기본값 또는 적절한 값
    '습도': 0,          # 기본값 또는 적절한 값
    '기타_변수1': 0,    # 기본값 또는 적절한 값
    '기타_변수2': 0,    # 기본값 또는 적절한 값
    '기타_변수3': 0,    # 기본값 또는 적절한 값
    '중심기압(hPa)': new_pressure_value  # 예측할 값
}], columns=X.columns)

# 데이터 스케일링
new_pressure_scaled = scaler.transform(new_pressure_df)

# 예측 수행
predicted_damage = best_regressor.predict(new_pressure_scaled)
print(f"예측된 피해량: {predicted_damage[0]}")

def categorize_damage(damage):
    if damage < 100:
        return "경미"
    elif 100 <= damage < 500:
        return "중간"
    else:
        return "심각"

# 예측된 피해량에 대한 피해 범주 판별
damage_category = categorize_damage(predicted_damage[0])
print(f"예측된 피해 범주: {damage_category}")

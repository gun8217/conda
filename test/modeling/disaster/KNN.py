from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
# 폰트 경로 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_prop = fm.FontProperties(fname=font_path, size=12)
plt.rcParams['font.family'] = font_prop.get_name()


# 데이터 준비
file_path = 'C:/Users/Administrator/Documents/conda/test/modeling/disaster/natural.csv'
dataset = pd.read_csv(file_path, encoding='euc-kr')

# 데이터 전처리
datas = dataset.copy()
datas = datas.drop(columns=['시작시간', '종료기간', '데이터기준일자'])

# 숫자형으로 변환
le_disaster = LabelEncoder()
datas['재해구분'] = le_disaster.fit_transform(datas['재해구분'])

# 데이터 분리
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

# 원본 데이터와 스케일링된 데이터 비교를 위한 설정
features = X.columns  # 특성 이름

# 원본 데이터와 스케일링된 데이터 준비
X_original = pd.DataFrame(X_train, columns=features)
X_scaled = pd.DataFrame(X_train_scaled, columns=features)

# 스케일링 전후 비교를 위한 그래프
plt.figure(figsize=(14, 8))

for i, feature in enumerate(features):
    plt.subplot(len(features), 1, i + 1)
    sns.histplot(X_original[feature], kde=True, label='스케일링 전', color='blue', alpha=0.6)
    sns.histplot(X_scaled[feature], kde=True, label='스케일링 후', color='red', alpha=0.6)
    plt.title(f'{feature}의 스케일링 전후 분포 비교')
    plt.xlabel('값')
    plt.ylabel('빈도')

plt.tight_layout()
plt.show()




knn_model = KNeighborsRegressor(n_neighbors=5)
knn_model.fit(X_train_scaled, y_train)

# 모델 평가
train_acc = knn_model.score(X_train_scaled, y_train)
print("훈련 정확도 :", train_acc)

pred = knn_model.predict(X_test_scaled) # 모델 테스트

test_acc = knn_model.score(X_test_scaled, y_test)
print("테스트 정확도 :", test_acc)

# Mean Squared Error 계산
mse = mean_squared_error(y_test, pred)
print(f"Mean Squared Error (MSE): {mse}")

# R² Score 계산
r2 = r2_score(y_test, pred)
print(f"R² Score: {r2}")
print()




# 모델 예측
y_train_pred = knn_model.predict(X_train_scaled)
y_test_pred = knn_model.predict(X_test_scaled)

def plot_predictions(y_true, y_pred, feature_names, title):
    plt.figure(figsize=(15, 10))
    for i, feature_name in enumerate(feature_names):
        plt.subplot(len(feature_names), 1, i + 1)
        plt.scatter(y_true[:, i], y_pred[:, i], alpha=0.5, color='blue')
        plt.plot([min(y_true[:, i]), max(y_true[:, i])], 
                 [min(y_true[:, i]), max(y_true[:, i])], 
                 color='red', linestyle='--')
        plt.xlabel('실제값')
        plt.ylabel('예측값')
        plt.title(f'{feature_name} 예측 결과')
    plt.tight_layout()
    plt.show()

# 타겟 변수 이름
feature_names = ['순간최대풍속', '일최대강우량(mm)', '사망', '실종', '부상', '재산피해규모(백만원)']

# 훈련 데이터 예측 결과 시각화
plot_predictions(y_train.values, y_train_pred, feature_names, '훈련 데이터: 실제값 vs 예측값')

# 테스트 데이터 예측 결과 시각화
plot_predictions(y_test.values, y_test_pred, feature_names, '테스트 데이터: 실제값 vs 예측값')





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

# KNN 모델을 사용하여 가장 가까운 이웃 찾기
distances, indices = knn_model.kneighbors(new_data_scaled)

# n_neighbors 갯수만큼의 이웃 데이터 추출
neighbors_data = dataset.iloc[indices[0]]

# 인코딩된 '재해구분' 데이터를 가져옴
encoded_disaster = datas.iloc[indices[0]]['재해구분']

# '재해구분'을 한글로 매핑
neighbors_data = neighbors_data.copy()  # 복사본을 생성
neighbors_data.loc[:, '재해구분'] = le_disaster.inverse_transform(encoded_disaster)

# 발생년도 추가 (시작시간에서 연도 추출)
neighbors_data.loc[:, '발생년도'] = pd.to_datetime(neighbors_data['시작시간']).dt.year

# 소멸기간 추가 (종료시간 - 시작시간)
start_time = pd.to_datetime(neighbors_data['시작시간'])
end_time = pd.to_datetime(neighbors_data['종료기간'])
neighbors_data.loc[:, '소멸기간'] = (end_time - start_time).dt.days

# 인덱스 및 불필요한 컬럼 제거
neighbors_data = neighbors_data.reset_index(drop=True)
neighbors_data = neighbors_data.drop(columns=['시작시간', '종료기간', '데이터기준일자'])


# 결과 출력
print(neighbors_data)

# CSV 파일로 저장
file_path2 = 'C:/Users/Administrator/Documents/conda/test/modeling/disaster/KNN.csv'
neighbors_data.to_csv(file_path2, index=False, encoding='utf-8-sig')
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import pandas as pd

# 데이터 준비
file_path = 'C:/Users/Administrator/Documents/conda/test/modeling/natural.csv'
natural = pd.read_csv(file_path, encoding='euc-kr')

# 전처리 및 특성 선택
data = natural.copy()
data = data.drop(columns=['시작시간', '종료기간', '데이터기준일자'])
data['발생년도'] = pd.to_datetime(data['시작시간'], format='%Y-%m-%d').dt.year
le_damage = LabelEncoder()
data['피해범주_encoded'] = le_damage.fit_transform(data['피해범주'])
X = data[['중심기압(hPa)']]
y = data['피해범주_encoded']

# 훈련 및 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# KNN 모델 사용
knn = KNeighborsClassifier(n_neighbors=5, algorithm='auto', p=2, weights='uniform')
knn.fit(X_train, y_train)

# 모델 평가
train_acc = knn.score(X_train, y_train)
print("훈련 정확도 :", train_acc)

y_pred = knn.predict(X_test)
print(classification_report(y_test, y_pred))

test_acc = knn.score(X_test, y_test)
print("테스트 정확도 :", test_acc)

cm = confusion_matrix(y_test, y_pred)
print(f"예측 결과 확인: {cm}")
print()

for attr in dir(knn):
    if not attr.startswith('__'):print(knn)
    break

print(knn.feature_names_in_)
print(knn.feature_importances_)
print()




from sklearn.model_selection import GridSearchCV

# 하이퍼파라미터 그리드 정의
param_grid = {
    'n_neighbors': [3, 5, 7, 10],
    'weights': ['uniform', 'distance'],
    'p': [1, 2]
}

# GridSearchCV 객체 생성
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)

# 모델 훈련
grid_search.fit(X_train, y_train)

# 최적 하이퍼파라미터 출력
print("Best parameters:", grid_search.best_params_)
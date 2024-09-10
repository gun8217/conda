from sklearn.tree import DecisionTreeClassifier

from utils import *

# 데이터 준비
natural, data, le_disaster, le_damage = dataLoad()

# 데이터 분할
X, X_train, X_test, y_train, y_test = dataSplit(data)

# 모델 훈련 학습 및 결과
desition_gini = modelAccPred(DecisionTreeClassifier(random_state=42), data)



# 새로운 중심기압 입력 예측
new_pressure = [[1005]]  # 예시 중심기압
new_pressure_df = pd.DataFrame(new_pressure, columns=['중심기압(hPa)'])
predicted_category = desition_gini.predict(new_pressure_df)
predicted_category_label = le_damage.inverse_transform(predicted_category)
print(f'입력된 중심기압 {new_pressure[0][0]}의 피해 범주는 {predicted_category_label[0]}입니다.')
print()



# 예측된 피해 범주에 따른 비슷한 중심기압의 자연재해 찾기
predicted_category_code = le_damage.transform(predicted_category_label)

# 필터링을 위한 정수형으로 변환된 '피해범주' 컬럼을 사용하여 데이터에서 비슷한 재해를 찾습니다.
similar_disasters = data[data['피해범주_encoded'] == predicted_category_code[0]].copy()

# '재해구분'을 원본 데이터에서 직접 가져와서 추가
# 매핑 딕셔너리 생성
disaster_mapping = dict(zip(le_disaster.transform(le_disaster.classes_), le_disaster.classes_))

# '재해구분'을 다시 한글로 변환
similar_disasters.loc[:, '재해구분'] = similar_disasters['재해구분_encoded'].map(disaster_mapping)

# NaN 값 처리 (예: '재해구분'이 NaN인 행 제거)
similar_disasters = similar_disasters.dropna(subset=['재해구분'])

# 피해 상황을 DataFrame 형태로 출력 (인덱스 번호 숨기기)
print("비슷한 중심기압의 자연재해와 피해 정보:")
output_file_path = 'C:/Users/user/Documents/conda/test/modeling/dicision_gini_1005.csv'
print(similar_disasters[['발생년도', '소멸기간', '재해구분', '중심기압(hPa)', '순간최대풍속',
                         '일최대강우량(mm)', '사망', '실종', '부상', '재산피해규모(백만원)']]
      .to_csv(output_file_path, index=False, encoding='utf-8-sig'))
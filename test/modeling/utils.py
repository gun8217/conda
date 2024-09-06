import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def dataLoad():
    file_path = 'C:/Users/Administrator/Documents/conda/test/modeling/natural.csv'
    datas = pd.read_csv(file_path, encoding='euc-kr')
    
    datas['시작시간'] = pd.to_datetime(datas['시작시간'], format='%Y-%m-%d')
    datas['종료기간'] = pd.to_datetime(datas['종료기간'], format='%Y-%m-%d')
    datas['발생년도'] = datas['시작시간'].dt.year
    datas['소멸기간'] = (datas['종료기간'] - datas['시작시간']).dt.days
    
    data = datas.copy()
    data = data.drop(columns=['시작시간', '종료기간', '데이터기준일자'])
    
    le_disaster = LabelEncoder() # 숫자형으로 변환
    data['재해구분_encoded'] = le_disaster.fit_transform(data['재해구분'])

    # 피해 범주 정의
    bins = [0, 980, 1000, 1020, 1040]  # 중심기압 구간
    labels = ['저압', '중저압', '중압', '고압']  # 범주
    data['피해범주'] = pd.cut(data['중심기압(hPa)'], bins=bins, labels=labels)

    le_damage = LabelEncoder()
    data['피해범주_encoded'] = le_damage.fit_transform(data['피해범주'])
    
    return datas, data, le_disaster, le_damage


def dataSplit(data):
    X = data[['중심기압(hPa)']]  # 피처
    y = data['피해범주_encoded']  # 타겟: 피해 범주

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.3,
                                                        random_state=42)
    
    return X, X_train, X_test, y_train, y_test


# desition_gini = DecisionTreeClassifier(random_state=42)
# desition_gini.fit(X_train, y_train)

# # 모델 평가
# train_acc = desition_gini.score(X_train, y_train)
# print("훈련 정확도 :", train_acc)

# y_pred = desition_gini.predict(X_test)
# print(classification_report(y_test, y_pred))

# test_acc = desition_gini.score(X_test, y_test)
# print("테스트 정확도 :", test_acc)

# cm = confusion_matrix(y_test, y_pred)
# print(f"예측 결과 확인:\n{cm}")
# print()

# for attr in dir(desition_gini):
#     if not attr.startswith('__'):print(desition_gini)
#     break
    
# print(desition_gini.criterion)
# print(desition_gini.feature_names_in_)
# print(desition_gini.feature_importances_)
# print()

# # 새로운 중심기압 입력 예측
# new_pressure = [[1005]]  # 예시 중심기압
# new_pressure_df = pd.DataFrame(new_pressure, columns=['중심기압(hPa)'])
# predicted_category = desition_gini.predict(new_pressure_df)
# predicted_category_label = le_damage.inverse_transform(predicted_category)
# print(f'입력된 중심기압 {new_pressure[0][0]}의 피해 범주는 {predicted_category_label[0]}입니다.')
# print()

# # 예측된 피해 범주에 따른 비슷한 중심기압의 자연재해 찾기
# predicted_category_code = le_damage.transform(predicted_category_label)

# # 필터링을 위한 정수형으로 변환된 '피해범주' 컬럼을 사용하여 데이터에서 비슷한 재해를 찾습니다.
# similar_disasters = data[data['피해범주_encoded'] == predicted_category_code[0]].copy()

# # '재해구분'을 원본 데이터에서 직접 가져와서 추가
# # 매핑 딕셔너리 생성
# disaster_mapping = dict(zip(le_disaster.transform(le_disaster.classes_), le_disaster.classes_))

# # '재해구분'을 다시 한글로 변환
# similar_disasters.loc[:, '재해구분'] = similar_disasters['재해구분_encoded'].map(disaster_mapping)

# # NaN 값 처리 (예: '재해구분'이 NaN인 행 제거)
# similar_disasters = similar_disasters.dropna(subset=['재해구분'])

# # 피해 상황을 DataFrame 형태로 출력 (인덱스 번호 숨기기)
# print("비슷한 중심기압의 자연재해와 피해 정보:")
# output_file_path = 'C:/Users/Administrator/Documents/conda/test/modeling/dicision_gini_1005.csv'
# print(similar_disasters[['발생년도', '소멸기간', '재해구분', '중심기압(hPa)', '순간최대풍속',
#                          '일최대강우량(mm)', '사망', '실종', '부상', '재산피해규모(백만원)']]
#       .to_csv(output_file_path, index=False, encoding='utf-8-sig'))




# import matplotlib.pyplot as plt
# from sklearn.tree import plot_tree
# from matplotlib import font_manager as fm

# # 폰트 경로 설정
# font_path = 'C:/Windows/Fonts/malgun.ttf'
# font_prop = fm.FontProperties(fname=font_path, size=12)
# plt.rcParams['font.family'] = font_prop.get_name()

# # 피처 이름과 클래스 이름을 문자열로 변환
# feature_names = [str(name) for name in X.columns]
# class_names = [str(label) for label in le_damage.classes_]

# # 결정 트리 시각화
# plt.figure(figsize=(7, 4), dpi=300)
# plot_tree(desition_gini, feature_names=feature_names, class_names=class_names, filled=True)
# plt.savefig('C:/Users/Administrator/Documents/conda/test/modeling/dicition_gini.png')
# plt.tight_layout()
# plt.show()
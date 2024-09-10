import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


def dataLoad():
    file_path = 'C:/Users/user/Documents/conda/test/modeling/disaster/natural.csv'
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


def modelAccPred(modelDeclaration, data):
    X, X_train, X_test, y_train, y_test = dataSplit(data)
    
    model = modelDeclaration
    model.fit(X_train, y_train)

    # 모델 평가
    train_acc = model.score(X_train, y_train)
    print("훈련 정확도 :", train_acc)

    y_pred = model.predict(X_test)

    test_acc = model.score(X_test, y_test)
    print("테스트 정확도 :", test_acc)
    
    report = classification_report(y_test, y_pred)
    print(f"예측 결과 확인:\n{report}")
    cm = confusion_matrix(y_test, y_pred)
    print(f"예측 결과 확인:\n{cm}")
    print()

    for attr in dir(model):
        if not attr.startswith('__'):print(model)
        break

    print(model.criterion)
    print(model.feature_names_in_)
    print(model.feature_importances_)
    print()
    
    return model
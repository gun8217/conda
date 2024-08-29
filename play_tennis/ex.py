import pandas as pd
import numpy as np

def feature_likelihoods(dataset, feature_name, target_values):
    """
    주어진 특성에 대한 각 값의 likelihood를 계산하여 데이터프레임으로 반환합니다.

    :param dataset: 데이터프레임
    :param feature_name: 특성의 열 이름
    :param target_values: 타겟 변수의 값 리스트
    :return: 특성 값에 대한 likelihood를 포함하는 데이터프레임
    """
    data = dataset[[feature_name] + target_values]
    states = data[feature_name].unique()
    
    n_total = {value: (dataset[dataset[target_values[0]] == value]).shape[0] for value in target_values}
    
    likelihoods_df = pd.DataFrame(index=target_values)
    
    for state in states:
        state_data = data[data[feature_name] == state]
        
        likelihoods = []
        for value in target_values:
            n_value = (state_data[target_values[0]] == value).sum()
            likelihood = n_value / n_total[value]
            likelihoods.append(likelihood)
        
        likelihoods_df[state] = likelihoods

    return likelihoods_df

def combined_feature_likelihoods(dataset, features, target_values):
    """
    여러 특성에 대한 likelihoods를 계산하여 개별 데이터프레임으로 반환합니다.

    :param dataset: 데이터프레임
    :param features: 처리할 특성 이름의 리스트
    :param target_values: 타겟 변수의 값 리스트
    :return: 모든 특성의 likelihood를 포함하는 데이터프레임 리스트
    """
    likelihoods_dfs = []
    
    for feature in features:
        likelihoods_df = feature_likelihoods(dataset, feature, target_values)
        likelihoods_df.index = [f"{feature} - {index}" for index in likelihoods_df.index]  # 인덱스에 특성명을 추가
        likelihoods_dfs.append(likelihoods_df)
    
    return likelihoods_dfs

# 예제 데이터프레임 생성
data = pd.DataFrame({
    'outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain'],
    'temp': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool'],
    'humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal'],
    'wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Strong', 'Strong'],
    'play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No']
})

# 처리할 특성 리스트
features = ['outlook', 'temp', 'humidity', 'wind']

# 타겟 변수 값 리스트
target_values = ['Yes', 'No']

# 모든 특성의 likelihood 계산
likelihoods_list = combined_feature_likelihoods(data, features, target_values)

# 각 특성의 likelihoods를 개별적으로 출력
for i, feature in enumerate(features):
    print(f"\nLikelihoods for '{feature}':")
    print(likelihoods_list[i])

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

import numpy as np
import pandas as pd


# 시계열 데이터를 회귀 문제로 변환
def prepare_data(series, window_size):
    X, y = [], []
    for i in range(len(series) - window_size):
        X.append(series[i:i + window_size])
        y.append(series[i + window_size])
    return np.array(X), np.array(y)


# 데이터 준비
file_path = 'C:/Users/user/Documents/conda/test/modeling/echo.csv'
dataset = pd.read_csv(file_path, encoding='euc-kr')
print(dataset.head())

# 데이터 전처리
datas = dataset.copy()
datas['월별'] = datas['구분']


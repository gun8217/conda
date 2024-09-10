from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

import pandas as pd
from utils import *

# 데이터 준비
file_path = 'C:/Users/user/Documents/conda/test/modeling/echo.csv'
dataset = pd.read_csv(file_path, encoding='euc-kr')

# 데이터 전처리
datas = dataset.copy()
datas['월별'] = datas['구분']

# 데이터 분리
X = datas.drop(columns=['구분', '월별'])
y = datas['월별']
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3, random_state=42)

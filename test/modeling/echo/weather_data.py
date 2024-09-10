import pandas as pd

# 데이터 준비
file_path = 'C:/Users/user/Documents/conda/test/modeling/echo/weather.csv'
dataset = pd.read_csv(file_path)
print(dataset.head(), dataset.shape)
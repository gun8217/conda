import numpy as np
import pandas as pd

df_kospi = pd.read_csv('https://raw.githubusercontent.com/jin0choi1216/dataset/main/KOSPI_stocks.csv', index_col = 0)
print(df_kospi.head())

mean = df_kospi['Marcap'].mean()
df_kospi['유형'] = df_kospi['Marcap'].apply(lambda data: '대형주' if data > mean else '소형주')
unique = np.unique(df_kospi['유형'], return_counts=True)
print(unique)
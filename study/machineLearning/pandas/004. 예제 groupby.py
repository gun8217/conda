import numpy as np
import pandas as pd

# groupby
df_krx = pd.read_csv("https://raw.githubusercontent.com/jin0choi1216/dataset/main/KRX_stocks.csv", index_col=0)
print(df_krx.head())

print(df_krx['Market'].unique())
# print(df_krx[['Market', 'ChagesRatio']].groupby('Market').mean())
# print(df_krx[['Market', 'ChagesRatio']].groupby('Market').max())
# print(df_krx[['Market', 'ChagesRatio']].groupby('Market').min())
print(df_krx[['Market', 'ChagesRatio']].groupby('Market').agg(['min', 'max', 'sum']))
print(df_krx[['Market', 'ChagesRatio', 'Stocks']].groupby('Market').agg(['min', 'max', 'sum']))
print(df_krx[['Market', 'ChagesRatio', 'Stocks']].groupby('Market').agg({
    'ChagesRatio':'min',
    'Stocks':'sum'
}))
print(df_krx[['Market', 'ChagesRatio', 'Stocks']].groupby('Market').agg({
    'ChagesRatio':['min', 'max'],
    'Stocks':'sum'
}))
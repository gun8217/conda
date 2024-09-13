import numpy as np
import pandas as pd

df_krx = pd.read_csv("https://raw.githubusercontent.com/jin0choi1216/dataset/main/KRX_stocks.csv", index_col=0)
# print(df_krx.head())

# 1. df_krx의 Marcap(시가총액)를 활용하여 시가총액 순위를 새로운 칼럼으로 정의 (칼럼명 : Marcap_rank)
#   - Marcap(시가총액)이 높을수록 낮은순위(1등에 가깝다.)
# 2. 순위데이터(Marcap_rank)를 활용하여 100위 이하는 large-cap, 100~300위는 mid-cap,
# 이외 순위는 small-cap으로 새로운 칼럼 선언(칼럼명 : Marcap_size)
# 3. Marcap_size(large-cap, mid-cap,small-cap) 별 수익률(ChagesRatio)의 평균을 출력

df_krx['Marcap_rank'] = df_krx['Marcap'].rank()
# print(df_krx['Marcap_rank'].head())

df_krx['Marcap_size'] = df_krx['Marcap_rank'].apply(
    lambda x: 'large-cap' if x <= 100 
    else 'mid-cap' if x <= 300 
    else 'small-cap'
)

print((df_krx['ChagesRatio'] < 0).any())
print()

print(df_krx.groupby('Marcap_size')['ChagesRatio'].mean())
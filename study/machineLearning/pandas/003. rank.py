import pandas as pd

# rank
df = pd.read_csv('https://raw.githubusercontent.com/jin0choi1216/dataset/main/market_fundamental_20230817.csv', index_col='티커')
print(df.head())

# df_kospi['랭크'] = df_kospi['Marcap'].rank(ascending=False)
# print(df_kospi['랭크'].head())

# 주당 순이익(EPS)이 0이상 기업 중 PER 순위 - EPS 순위의 차이가 가장 적은 10개의 기업을 출력
# - PER는 낮을 수록 숫자가 낮은 순위
# - EPS는 높을 수록 숫자가 낮은 순위

df_filter = df[df['EPS'] > 0]

df_filter['PER_rank'] = df_filter['PER'].rank(ascending=True) # true는 기본값이므로 설정되어 있으므로 생략 가능
df_filter['EPS_rank'] = df_filter['EPS'].rank(ascending=False)

df_filter['Rank_diff'] = abs(df_filter['PER_rank'] - df_filter['EPS_rank'])
top_10 = df_filter.sort_values(by='Rank_diff').head(10)
print(top_10)
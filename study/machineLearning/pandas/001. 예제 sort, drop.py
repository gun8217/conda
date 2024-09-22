import pandas as pd

dates = pd.date_range('20240717', periods=3)
prices = {
    'SK텔레콤' : [44000, 44500, 45000],
    '삼성전자' : [70100, 70200, 70300],
    'LG전자' : [85000, 85500, 86000],
    'POSCO' : [450000, 455000, 460000]
}
df2 = pd.DataFrame(prices, index=dates)
print(df2)
print()

df2['LG화학'] = [500000, 500500, 501000]
df2 = df2.sort_values(by='삼성전자', ascending=False)
df2 = df2.drop(['LG전자'], axis=1)
print(df2)
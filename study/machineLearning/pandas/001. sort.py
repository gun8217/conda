# 내림차순 ascending=False
# sort_values - 열 기준 정렬 : DataFrame.sort_values(by='열이름', ascending=True, inplace=False)
# sort_index - 인덱스 기준 정렬 : DataFrame.sort_index(ascending=True, inplace=False)

import pandas as pd

data = {
    'A': [3, 1, 2],
    'B': [6, 4, 5]
}
df = pd.DataFrame(data)
print(df)
print()

# 열 'A'를 기준으로 오름차순 정렬
sort_values = df.sort_values(by='A')
print(f"{sort_values = }\n")

# 인덱스를 기준으로 내림차순 정렬
sort_index = df.sort_index(ascending=False)
print(f"{sort_index = }\n")
# loc 라벨 사용, iloc 정수 인덱스 사용
# loc 끝 인덱스 포함, iloc 끝 인덱스 미포함

import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data, index=['a', 'b', 'c'])
print(df)
print()

print(df.loc[['a', 'c'], 'A'])
print()

print(df.iloc[:-1, -1])
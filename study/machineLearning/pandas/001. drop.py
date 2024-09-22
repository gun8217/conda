# inplace=False(기본값) : 새로운 데이터프레임 반환
# inplace=True : 원본 데이터프레임 변경

import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)
print(df)
print()

# 행 인덱스 1 제거
drop_row = df.drop(labels=1)
print(f"{drop_row = }\n")

# 열 'B' 제거
drop_column = df.drop(labels='B', axis=1)
print(f"{drop_column = }\n")
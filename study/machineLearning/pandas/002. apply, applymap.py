# apply : 데이터프레임의 행 또는 열 요소에 함수 적용
# applymap : 전체 데이터프레임에 함수 적용

import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)
print(df)
print()


def row_sum(row):
    return row.sum()


# 행에 함수 적용
apply_row_sum = df.apply(row_sum, axis=1)
print(f"{apply_row_sum = }\n")


def mul_two(x):
    return x * 2


# 열에 함수 적용
apply_column = df.apply(mul_two)
print(f"{apply_column = }\n")

# 특정 열 'A'에만 함수 적용
apply_column_A = df['A'].apply(mul_two)
print(f"{apply_column_A = }\n")


def even_or_odd(x):
    return 'Even' if x % 2 == 0 else 'Odd'


# 각 요소의 짝수/홀수 판단 적용
applymap = df.applymap(even_or_odd)
print(f"{applymap = }\n")
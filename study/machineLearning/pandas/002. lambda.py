import pandas as pd

# 데이터프레임 생성
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)
print(df)
print()

# 각 요소에 2를 곱하는 lambda 함수 사용
apply_lambda = df.apply(lambda x: x * 2)
print(f"{apply_lambda = }\n")

# 열 'A'의 각 요소에 3을 더하는 lambda 함수 사용
apply_lambda_A = df['A'].apply(lambda x: x + 3)
print(f"{apply_lambda_A = }\n")

# 각 행의 합을 계산하는 lambda 함수 사용
apply_lambda_row = df.apply(lambda row: row.sum(), axis=1)
print(f"{apply_lambda_row = }\n")

# 각 요소가 짝수인지 홀수인지 판단하는 lambda 함수 사용
applymap_lambda = df.applymap(lambda x: 'Even' if x % 2 == 0 else 'Odd')
print(f"{applymap_lambda = }\n")
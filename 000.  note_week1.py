data_a, data_b = [1, 2, 3], [10, 20, 30]

# 상수 합 과 평균
constant = 10
sum_ = sum(a + constant for a in data_a)
print(f"상수 합 : {sum_ = }")
mean_ = sum_ / len(data_a)
print(f"상수 합의 평균 : {mean_ = }\n")

# squared error
squared_error = [(a - b)**2 for a, b in zip(data_a, data_b)]
print(f"제곱오차(data 차이의 제곱) : {squared_error = }\n")

# mean squared error
mse = sum(squared_error) / len(data_a)
print(f"제곱오차 합의 평균 : {mse}\n")

# normalizing vector
a_norm = sum(a**2 for a in data_a)**0.5
print(f"data 제곱 합의 루트 : {a_norm = }")
normalizing_vector = [a / a_norm for a in data_a]
a_norm = sum(a**2 for a in normalizing_vector)**0.5
print(f"다시 norm 계산 : {a_norm = }")

# dot product
dot_prod = sum(a * b for a, b in zip(data_a, data_b))
print(f"내적(곱한 후 합) : {dot_prod = }\n")

# Euclidean distance
e_dist = sum((a - b)**2 for a, b in zip(data_a, data_b))**0.5
print(f"거리 차이 제곱 합에 루트 : {e_dist = }\n")

# mean subtraction
sub_mean = sum(data_b) / len(data_b)
sub_mean_= sum(b - sub_mean for b in data_b) / len(data_b)
print(f"평균 제거 후 평균(0 만들기) : {sub_mean_ = }\n")

# 표준편차
b_mean = sum(data_b) / len(data_b)
print(f"평균 : {b_mean = }")
sum_squared = sum((b - b_mean)**2 for b in data_b)
print(f"편차(값 - 평균) 제곱의 합 : {sum_squared = }")
squared_var = sum_squared  / len(data_b)
print(f"분산(편차 제곱의 합의 평균) : {squared_var = }")
squared_std = squared_var**0.5
print(f"표준편차(분산에 루트) : {squared_std = }\n")

# standardization
data_b = [(b - b_mean) / squared_std for b in data_b]
print(f"정규식(편차를 표준편차로 나누기) 후 data : {data_b = }")
b_mean = sum(data_b) / len(data_b)
sum_squared = sum((b - b_mean)**2 for b in data_b)
squared_var = sum_squared  / len(data_b)
squared_std = squared_var**0.5
print(f"정규식 후 분산(0) : {squared_var = }")
print(f"정규식 후 표준편차(1) : {squared_std = }\n")
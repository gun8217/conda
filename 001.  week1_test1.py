data_a, data_b = [1, 2, 3], [10, 20, 30]

# 합
sum_ = sum(data_a)
print(f"{sum_ = }\n")

# 평균
mean_ = sum_ / len(data_a)
print(f"{mean_ = }\n")

# 상수더하기
count = 10
count_sum = [b + count for b in data_b]
print(f"{count_sum = }\n")

# 상수 더해서 평균
count_mean = sum(count_sum) / len(count_sum)
print(f"{count_mean = }\n")

# 편차 제곱
b_mean = sum(data_b) / len(data_b)
squared_mean = [(b - b_mean)**2 for b in data_b]
print(f"{squared_mean = }\n")

# 분산
squared_var = sum(squared_mean) / len(squared_mean)
print(f"{squared_var = }\n")

# 표준편차
squared_std = squared_var**0.5
print(f"{squared_std = }\n")

# Squared Error
squared_error = [(a - b)**2 for a, b in zip(data_a, data_b)]
print(f"{squared_error = }\n")

# Mean Squared Error
mse = sum(squared_error) / len(squared_error)
print(f"{mse = }\n")

# Mean Subtraction
mean_subtraction = sum((a - mean_) for a in data_a) / len(data_a)
print(f"{mean_subtraction = }\n")

# Standardization
standardization = [(b - b_mean) / squared_std for b in data_b]
print(f"{standardization = }")
b_mean = sum(standardization) / len(standardization)
squared_mean = [(b - b_mean)**2 for b in data_b]
squared_var = sum(squared_mean) / len(squared_mean)
squared_std = squared_var**0.5
print(f"{squared_std = }\n")

# Vecotr Addition, Subtraction
v_addition = [a + b for a, b in zip(data_a, data_b)]
print(f"{v_addition = }")
v_subtraction = [a - b for a, b in zip(data_a, data_b)]
print(f"{v_subtraction = }\n")

# Scalar
count = 5
scalar = [a + count for a in data_a]
print(f"{scalar = }\n")

# Vecotr Norm
vertor_norm = sum([a**2 for a in data_a])**0.5
print(f"{vertor_norm = }")
# Normalizing Vector
normalizing_vector = [a / vertor_norm for a in data_a]
vertor_norm = sum([a**2 for a in normalizing_vector])**0.5
print(f"{vertor_norm = }\n")

# Dot Product
dot_product = sum(a * b for a, b in zip(data_a, data_b))
print(f"{dot_product = }\n")

# Euclidean Distance
euclidean_distance = sum((a - b)**2 for a, b in zip(data_a, data_b))**0.5
print(f"{euclidean_distance = }\n")
data_a, data_b = [1, 2, 3], [10, 20, 30]

# 합
b_sum = sum(data_b)
print(f"{b_sum = }")

# 평균
b_mean = b_sum / len(data_b)
print(f"{b_mean = }")

# 상수더하기
number = 3
num_sum = [a + number for a in data_a]
print(f"{num_sum = }")

# 상수 더해서 평균
num_mean = sum(num_sum) / len(num_sum)
print(f"{num_mean = }\n")

# Squared Error
squared_error = [(a - b)**2 for a, b in zip(data_a, data_b)]
print(f"{squared_error = }")

# Mean Squared Error
mse = sum(squared_error) / len(squared_error)
print(f"{mse = }\n")

# Mean Subtraction
mean_subtraction = sum([(b - b_mean) for b in data_b]) / len(data_b)
print(f"{mean_subtraction = }\n")

# 편차 제곱
squared_mean = [(b - b_mean)**2 for b in data_b]
print(f"{squared_mean = }")
# 분산
squared_var = sum(squared_mean) / len(squared_mean)
print(f"{squared_var = }")
# 표준편차
squared_std = squared_var**0.5
print(f"{squared_std = }")
# Standardization
data_b = [(b - b_mean) / squared_std for b in data_b]
b_mean = sum(data_b) / len(data_b)
squared_mean = [(b - b_mean)**2 for b in data_b]
squared_var = sum(squared_mean) / len(squared_mean)
squared_std = squared_var**0.5
print(f"{squared_std = }\n")

# Vecotr Addition, Subtraction
vecotr_addition = [(a + b) for a, b in zip(data_a, data_b)]
print(f"{vecotr_addition = }")
vecotr_subtraction = [(a - b) for a, b in zip(data_a, data_b)]
print(f"{vecotr_subtraction = }")

# Scalar
scalar = [a + number for a in data_a]
print(f"{scalar = }\n")

# Vecotr Norm
vecotr_norm = sum(a**2 for a in data_a)**0.5
print(f"{vecotr_norm = }")
# Normalizing Vector
normalizing_vector = [a / vecotr_norm for a in data_a]
vecotr_norm = sum(a**2 for a in normalizing_vector)**0.5
print(f"{vecotr_norm = }\n")

# Dot Product
dot_product = sum((a * b) for a, b in zip(data_a, data_b))
print(f"{dot_product = }")

# Euclidean Distance
euclidean_distance = sum((a - b)**2 for a, b in zip(data_a, data_b))**0.5
print(f"{euclidean_distance = }")
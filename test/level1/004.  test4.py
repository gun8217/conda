from module import *

# 합
input_data = int(input('plus number : '))
result = sum(num for num in range(1, input_data + 1))
print(f"{result = }\n")

# 평균
dataBox1 = func_score()
dataBox_mean = sum(dataBox1) / len(dataBox1)
print(f"{dataBox_mean = }\n")

# 상수더하기 +10
dataBox2 = func_score()
print(f"{dataBox2 = }")
plus_sum = [data + 10 for data in dataBox2]
print(f"{plus_sum = }\n")

# Squared Error(2)
data_a, data_b = [1, 2, 3], [10, 20, 30]
squared_error = [(a - b)**2 for a, b in zip(data_a, data_b)]
print(f"{squared_error = }")

# Mean Squared Error

# Mean Subtraction

# 편차 제곱

# 분산

# 표준편차

# Standardization

# Vecotr Addition, Subtraction

# Scalar(1 + 상수)

# Vecotr Norm

# Normalizing Vector

# Dot Product(2)

# Euclidean Distance(2)
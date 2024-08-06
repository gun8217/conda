data_a, data_b = [1, 2, 3], [10, 20, 30]

# 평균
b_mean = sum(data_b) / len(data_b)

# Squared Error : 2
s_error = [(a - b)**2 for a, b in zip(data_a, data_b)]
print(f"Squared Error : {s_error}")
# Mean Squared Error
mse = sum(s_error) / len(s_error)
print(f"Mean Squared Error : {mse}\n")

# Mean Subtraction : 1
m_sub = sum((b - b_mean) for b in data_b) / len(data_b)
print(f"Mean Subtraction : {m_sub}\n")

# 편차 제곱 : 1
squared_mean = [(b - b_mean)**2 for b in data_b]
print(f"편차 제곱 : {squared_mean}")
# 분산
squared_var = sum(squared_mean) / len(squared_mean)
print(f"분산 : {squared_var}")
# 표준편차
squared_std = squared_var**0.5
print(f"표준편차 : {squared_std}")

# Standardization
data_b = [(b - b_mean) / squared_std for b in data_b]
b_mean = sum(data_b) / len(data_b)
squared_mean = [(b - b_mean)**2 for b in data_b]
squared_var = sum(squared_mean) / len(squared_mean)
squared_std = squared_var**0.5
print(f"정규화 후 표준편차 : {squared_std}\n")

# Vecotr Norm : 1
v_norm = sum([a**2 for a in data_a])**0.5
print(f"Vecotr Norm : {v_norm}")
# Normalizing Vector
data_a = [a / v_norm for a in data_a]
v_norm = sum([a**2 for a in data_a])**0.5
print(f"Normalizing 후 norm : {v_norm}")
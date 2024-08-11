from module import *

# # 합
# input_data = int(input('plus number : '))
# result = sum(num for num in range(1, input_data + 1))
# print(f"{result = }\n")

# # 평균
# dataBox1 = func_input()
# dataBox_mean = sum(dataBox1) / len(dataBox1)
# print(f"{dataBox_mean = }\n")

# # 상수더하기 +10
# dataBox2 = func_input()
# print(f"{dataBox2 = }")
# plus_sum = [data + 10 for data in dataBox2]
# print(f"{plus_sum = }\n")

# # Squared Error(2)
# data_a, data_b = random_datas2(3, 3)
# print(f"{data_a = }, {data_b = }")
# squared_error = [(a - b)**2 for a, b in zip(data_a, data_b)]
# print(f"{squared_error = }")

# # Mean Squared Error : Squared Error 합의 평균
# mse = func_mean(squared_error)
# print(f"{mse = }")

# # Mean Subtraction(1)
# dataBox3 = random_datas(5)
# print(f"before : {dataBox3 = }")
# mean_sub = func_mean(dataBox3)
# dataBox3 = [data - mean_sub for data in dataBox3]
# print(f"after : {dataBox3 = }")
# mean_sub = func_mean(dataBox3)
# if close_to_zero(mean_sub): mean_sub = 0.0
# print(f"final : {mean_sub = }")

# # Standardization
# dataBox4 = random_datas(5)
# stdz_data = func_stdz(dataBox4)
# stdz_std = func_std(stdz_data)
# if close_to_zero(stdz_std - 1.0): stdz_std = 1.0
# print(f"{stdz_std = }")

# # Normalizing Vector
# dataBox5 = random_datas(5)
# nomalizing_vector = func_norm_1(dataBox5)
# print(f"{nomalizing_vector = }")

# Dot Product(2)
# data_a, data_b, data_c = random_datas2(3, 3, 3)
# print(data_a, data_b, data_c)
# dot_prod = func_dot(data_a, data_b, data_c)
# print(func_dot(data_a, data_b, data_c))

# Euclidean Distance(2)
data_a, data_b, data_c = random_datas2(3, 3, 3)
euclidean_distance = func_eucDist(data_a, data_b, data_c)
print(f"{euclidean_distance = }")
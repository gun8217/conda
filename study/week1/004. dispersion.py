###### 분산 : 편차 제곱의 평균(제평평제)
datas = [10, 20, 30, 40, 50]

# 제곱의 평균
data_squared = [data**2 for data in datas]
mean_of_squared = sum(data_squared) / len(datas)

# 평균의 제곱
data_mean = sum(datas) / len(datas)
squared_of_mean = data_mean**2

# 제곱의 평균 - 평균의 제곱
data_var = mean_of_squared - squared_of_mean
print(f"{data_var = }")
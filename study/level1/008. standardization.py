###### 표준 정규 분포 : 평균=0, 표준편차=1
datas = [10, 20, 30, 40, 50]

# 표준편차
data_mean = sum(datas) / len(datas)
sum_squared_dev = sum((data - data_mean)**2 for data in datas)
data_var = sum_squared_dev / len(datas)
data_std = data_var**0.5

# standardization
for data_idx, data in enumerate(datas):
    datas[data_idx] = (data - data_mean) / data_std
 
# 다시 표준편차
data_mean = sum(datas) / len(datas)
sum_squared_dev = sum((data - data_mean)**2 for data in datas)
data_var = sum_squared_dev / len(datas)
data_std = data_var**0.5

print(f"{data_mean = }")
print(f"{data_std = }")
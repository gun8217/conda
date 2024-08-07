###### 편차 제곱
datas = [10, 20, 30, 40, 50]

# 평균
data_mean = sum(datas) / len(datas)

# 각 데이터에서 평균을 빼고 제곱
squared_diffs = [(data - data_mean)**2 for data in datas]
print(f"{squared_diffs = }")
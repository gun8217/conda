###### 벡터 덧셈 뺄셈
u, v = [1, 2, 3], [10, 20, 30]

# 덧셈
sum_ = [u_el + v_el for u_el, v_el in zip(u, v)]
print(f"{sum_ = }")

# 뺄셈
sub_ = [u_el - v_el for u_el, v_el in zip(u, v)]
print(f"{sub_ = }")


###### Norm
datas = [1, 2, 3]
# norm 구하기 : 벡터의 크기 또는 길이를 측정하는 값
data_norm = sum(data**2 for data in datas)**0.5
print(f"{data_norm = }")

# normalizing vector : 크기 1(벡터의 방향성을 유지하면서 크기를 표준화할 때 유용)
data_norm = [data / data_norm for data in datas]
data_norm = sum(data**2 for data in data_norm)**0.5
print(f"{data_norm = }")
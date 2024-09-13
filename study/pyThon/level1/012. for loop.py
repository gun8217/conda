###### for loop
data_a, data_b = [1, 2, 3], [10, 20, 30]

for el in data_a:
    print(f"el에 각각의 data_a 값을 담아 data_a index 갯수만큼 돌려라 : {el}")
print() # 줄바꿈 용도

# 합
sum1 = 0
for a in data_a:
    sum1 += a
print(f"가독성 : {sum1}") # 다수 참여 프로젝트

sum2 = 0
for b in data_b: sum2 += b
print(f"간결성 : {sum2}\n") # 단독 프로젝트

# vector norm : 제곱 합의 루트
sum_squared = 0
for b in data_b:
    sum_squared += b**2
vector_norm = sum_squared**0.5
print(f"{vector_norm = }\n")

# 표준편차 : 분산(편차 제곱의 평균)의 루트
b_mean = sum(data_b) / len(data_b)
print(f"평균 : {b_mean = }")
sum_squared2 = 0
for b in data_b:
    sum_squared2 += (b - b_mean)**2
print(f"편차 제곱의 합(각 data의 평균 뺀 제곱) : {sum_squared2 = }")
squared_var = sum_squared2 / len(data_b)
print(f"분산(편차 제곱 합의 평균) : {squared_var = }")
squared_std = squared_var**0.5
print(f"표준편차(분산의 루트) : {squared_std = }\n")
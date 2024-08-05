###### 평균 제거 : 평균을 0으로 만들기(평균 중심화, 정규화 및 스케일링, 왜곡 감소)
datas = [10, 20, 30, 40, 50]

# 평균 계산
data_mean = sum(datas) / len(datas)

# 각 데이터의 평균 빼기
for i in range(len(datas)):
    datas[i] -= data_mean

# 다시 평균 계산
data_mean = sum(datas) / len(datas)
print(f"{data_mean = }")
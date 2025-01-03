import numpy as np

# 평균이 [5, 3]이고 표준편차가 [1, 1]인 2차원 정규 분포 : y 방향이 1인 dataset 만들기
n_data = 100

x_data = np.random.normal(loc=5, scale=1, size=(n_data,))
y_data = np.random.normal(loc=3, scale=1, size=(n_data,))
print(x_data.shape)
x_data = x_data.reshape(-1, 1) # y방향으로 1로 나머지를 자동으로
y_data = y_data.reshape(-1, 1)
print(x_data.shape)
# data_ = np.hstack([x_data, y_data])
data_ = np.concatenate((x_data, y_data), axis=1)
print(data_.shape)

data = np.random.normal(loc=[5, 3], scale=[1, 1], size=(n_data, 2))
print(np.mean(data, axis=0))
print(np.std(data, axis=0))
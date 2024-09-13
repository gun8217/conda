import numpy as np
import matplotlib.pyplot as plt

# # 모든값이 각 0, 1, 2, 3 모양이 각 (100,) 총(400,)인 ndarray
# zeros = np.zeros(100, dtype=int)
# ones = np.ones(100, dtype=int)
# twos = np.full(100, 2, dtype=int)
# threes = np.full(100, 3, dtype=int)

# # 연결하여 (400,) ndarray 생성
# y = np.concatenate([zeros, ones, twos, threes])

n_class = 4
n_data = 100

# data_list = []
# for idx in range(n_class):
#     data = np.full(n_data, idx)
#     data_list.append(data)
    
# y = np.concatenate(data_list)

data = []
for idx in range(n_class):
    data_ = idx * np.ones(n_data,)
    data.append(data_)
y = np.hstack(data)

print(y.shape)
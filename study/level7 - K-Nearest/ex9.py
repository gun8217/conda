import numpy as np
import matplotlib.pyplot as plt

n_classes = 4
n_data = 100

# zeros = np.zeros(n_data)
# ones = np.ones(n_data)
# full2 = np.full(n_data, 2)
# full3 = np.full(n_data, 3)
# datas = np.hstack([zeros, ones, full2, full3])
# print(datas, datas.shape)

# data = []
# for class_idx in range(n_classes):
#     data_ = np.full(shape=(n_data,), fill_value=class_idx)
#     data.append(data_)

# data = np.hstack(data)
# print(data.shape)

data = []
for class_idx in range(n_classes):
    data_ = class_idx * np.ones(n_data,)
    data.append(data_)
# data = np.hstack(data)
data = np.concatenate(data)
print(data.shape)


# fig, ax = plt.subplots(figsize=(5, 5))


# fig.tight_layout()
# plt.show()
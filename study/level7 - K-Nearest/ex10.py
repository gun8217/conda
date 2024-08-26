import numpy as np
import matplotlib.pyplot as plt

# 4개의 class(0,1,2,3)를 가지는 dataset 만들기 : X:(400, 2), y:(100,)
n_data = 100
n_class = 4
n_feature = 2
cmap = plt.get_cmap('tab10')
colors = [cmap(i) for i in range(n_class)]

centroid = np.random.uniform(-10, 10, (2,))
data, centroids = [], []
for class_idx in range(n_class):
    data_ = class_idx * np.random.normal(centroid, 1, (n_data, 2))
    data.append(data_)
data = np.concatenate(data)
print(data, data.shape)

# fig, ax = plt.subplots(figsize=(7, 7))
# for class_idx in range(n_class):
#     ax.scatter(centroid[0], centroid[1],
#                s=100,
#                c='black',
#                marker='x')
#     ax.scatter(data[:, 0], data[:, 1],
#                facecolor='None',
#                alpha=0.5,
#                edgecolor=colors[class_idx])


# fig.tight_layout()
# plt.show()
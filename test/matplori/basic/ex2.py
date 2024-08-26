import numpy as np
import matplotlib.pyplot as plt

# 여섯 개의 클래스가 있으며, 각 클래스는 100개의 2차원 데이터 포인트로 이루어져 있습니다.
# 각 클래스의 중심점은 다음 좌표들입니다:
# 클래스 : [0, 0], [8, 8], [-8, 8], [8, -8], [-8, -8], [0, 10]
# 각 데이터 포인트는 중심점을 기준으로 표준편차가 3.0인 정규 분포를 따릅니다.
# 생성한 데이터를 산점도로 시각화하고, 각 클래스의 데이터 포인트를 서로 다른 색으로 구분하여 표시하세요.
# 각 클래스의 중심점을 별도의 마커로 표시하고, 중심점의 마커 모양을 다각형('D', 's', '^', 'P', 'h', '*')으로 설정하세요. 각 클래스의 중심점에 대해 서로 다른 마커 모양을 사용하세요.
# 그래프의 제목을 "Advanced Class Scatter Plot with Diverse Centroids"로 설정하세요.
# 그래프의 x축과 y축 범위를 각각 [-15, 15]로 설정하세요.
# 힌트: np.random.normal, plt.scatter, plt.title, plt.xlabel, plt.ylabel, ax.set_xlim, ax.set_ylim을 활용하세요.

n_class = 6
n_data = 100
centroids = [[0, 0], [8, 8], [-8, 8], [8, -8], [-8, -8], [0, 10]]
cmap = plt.get_cmap('tab10')
colors = [cmap(i) for i in range(n_class)]
marks = ['D', 's', '^', 'P', 'h', '*']

data = []
for idx in range(n_class):
    data_ = np.random.normal(loc=centroids[idx], scale=3, size=(n_data, 2))
    data.append(data_)
datas = np.vstack(data)
print(datas.shape)

fig, ax = plt.subplots(figsize=(7, 7))
    
for i in range(n_class):
    ax.scatter(data[i][:, 0], data[i][:, 1], color=colors[i], alpha=0.5)
    
for i, centroid in enumerate(centroids):
    ax.scatter(centroid[0], centroid[1], color=colors[i], s=250, marker=marks[i])

ax.set_title('Advanced Class Scatter Plot with Diverse Centroids')
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_xlim = ([-15, 15])
ax.set_ylim = ([-15, 15])

fig.tight_layout()
plt.show()
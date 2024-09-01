# 히트맵 (Heatmap)

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 생성
data = np.random.rand(10, 10)

# 히트맵 그리기
sns.heatmap(data, cmap='viridis', annot=True)
plt.title('Heatmap Example')
plt.show()
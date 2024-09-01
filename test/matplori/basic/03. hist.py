# 히스토그램 (Histogram)

import numpy as np
import matplotlib.pyplot as plt

# 데이터 생성
data = np.random.normal(loc=0, scale=1, size=1000)

# 히스토그램 그리기
plt.hist(data, bins=30, color='green', edgecolor='black', alpha=0.7)
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
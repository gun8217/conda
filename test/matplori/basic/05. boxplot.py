# 박스 플롯 (Box Plot)

import numpy as np
import matplotlib.pyplot as plt

# 데이터 생성
data = [np.random.normal(loc=0, scale=1, size=100) for _ in range(3)]

# 박스 플롯 그리기
plt.boxplot(data, labels=['Group 1', 'Group 2', 'Group 3'])
plt.title('Box Plot Example')
plt.ylabel('Value')
plt.grid(True)
plt.show()
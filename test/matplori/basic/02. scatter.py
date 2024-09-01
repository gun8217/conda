# 산점도 (Scatter Plot)

import numpy as np
import matplotlib.pyplot as plt

# 데이터 생성
x = np.random.rand(100)
y = np.random.rand(100)

# 산점도 그리기
plt.scatter(x, y, c='red', marker='x')
plt.title('Scatter Plot Example')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
# 선 그래프 (Line Plot)

import numpy as np
import matplotlib.pyplot as plt

# 데이터 생성
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# 선 그래프 그리기
plt.plot(x, y, label='Sine Wave', color='blue', linestyle='-', marker='o')
plt.title('Line Plot Example')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
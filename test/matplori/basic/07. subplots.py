# 서브플롯 (Subplots) : 여러 그래프를 하나의 그림에 배치

import numpy as np
import matplotlib.pyplot as plt

# 데이터 생성
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 서브플롯 그리기
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# 첫 번째 서브플롯
axs[0].plot(x, y1, color='blue')
axs[0].set_title('Sine Wave')
axs[0].set_xlabel('x')
axs[0].set_ylabel('sin(x)')

# 두 번째 서브플롯
axs[1].plot(x, y2, color='red')
axs[1].set_title('Cosine Wave')
axs[1].set_xlabel('x')
axs[1].set_ylabel('cos(x)')

plt.tight_layout()
plt.show()
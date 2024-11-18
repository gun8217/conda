import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from utils03 import Model, BCELoss

n_data = 100
threshold = 1

rng = np.random.default_rng()
x = rng.normal(threshold, 1, n_data)
noise = 0.3 * rng.normal(0, 1, n_data)
y = ((x + noise) > threshold).astype(int)

fig, ax = plt.subplots(dpi=200)
ax.scatter(x, y, alpha=0.5)

model = Model()
loss_function = BCELoss()
x_lim = ax.get_xlim()
x_model = np.linspace(x_lim[0], x_lim[1], 100)
y_model = model.forward(x_model)

cmap = matplotlib.colormaps['rainbow']
colors = cmap(np.linspace(0, 1, len(x)))
ax.plot(x_model, y_model, color=colors[0], lw=3)

lr = 0.1
for data_idx, (x_, y_) in enumerate(zip(x, y)):
    # 순전파: 예측값 계산
    pred = model.forward(x_)
    
    # 손실 계산: BCE 손실 함수 적용
    J = loss_function.forward(y_, pred)
    
    # 역전파: 손실 함수의 기울기 계산
    dJ_dpred = loss_function.backward()
    
    # 가중치 업데이트: 기울기를 사용해 가중치 조정
    model.backward(dJ_dpred, lr)
    
    # 학습 과정 시각화
    y_model = model.forward(x_model)
    ax.plot(x_model, y_model, color=colors[data_idx], alpha=0.5, lw=1)
    
ax.axhline(y=0, color='gray', lw=1, ls='--')
ax.axvline(x=threshold, color='gray', lw=1, ls='--')

plt.tight_layout()
plt.show()
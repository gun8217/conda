import numpy as np
import matplotlib.pyplot as plt

# 𝑓(𝑥)=2𝑥**2 함수 정의
def f(x): return 1/10 * x**2

# 𝑑𝑓/𝑑𝑥=4𝑥 도함수 정의
def df_dx(x): return 1/5 * x

x = 3
ITERATIONS = 20

# 업데이트되는 x, y를 저장하기 위한 list : 초기값을 먼저 저장해둬야 함
x_track, y_track = [x], [f(x)]

print(f"Initial x: {x}")


for iter in range(ITERATIONS):
    # 현재 𝑥 값에서의 기울기(도함수 값) 계산
    dy_dx = df_dx(x)
    x = x - dy_dx
    
    # 업데이트된 𝑥 값과 그에 따른 함수 값을 각각 리스트에 추가
    x_track.append(x)
    y_track.append(f(x))
    
    print(f"{iter + 1}-th x: {x:.4f}")

fig, axes = plt.subplots(2, 1, figsize=(10, 5))
function_x = np.linspace(-5, 5, 100)
function_y = f(function_x)

# x-y 그래프
axes[0].plot(function_x, function_y)
axes[0].scatter(x_track, y_track,
                c=range(ITERATIONS + 1), cmap='rainbow')
axes[0].set_xlabel("x", fontsize=15)
axes[0].set_ylabel("y", fontsize=15)

# 반복에 따른 x 값 변화 그래프
axes[1].plot(x_track, marker='o')
axes[1].set_xlabel("Iteration", fontsize=15)
axes[1].set_ylabel("x", fontsize=15)

fig.tight_layout()
plt.show()
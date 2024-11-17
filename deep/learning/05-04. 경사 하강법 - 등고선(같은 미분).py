import numpy as np
import matplotlib.pyplot as plt

def f(x1, x2): return x1**2 + x2**2
def df_dx(x): return 2*x

x1, x2 = 3, -2
ITERATIONS = 10
LR = 0.1
x1_track, x2_track = [x1], [x2]

for iter in range(ITERATIONS):
    dy_dx1 = df_dx(x1)
    dy_dx2 = df_dx(x2)
    x1 = x1 - LR * dy_dx1
    x2 = x2 - LR * dy_dx2
    x1_track.append(x1)
    x2_track.append(x2)
 
function_x1 = np.linspace(-5, 5, 100)
function_x2 = np.linspace(-5, 5, 100)
function_X1, function_X2 = np.meshgrid(function_x1, function_x2)
function_Y = np.log(f(function_X1, function_X2))

fig, ax = plt.subplots(figsize=(10, 10))
ax.contour(function_X1, function_X2, function_Y,
           levels=100, cmap='Reds_r')
ax.plot(x1_track, x2_track, marker='o')
ax.set_xlabel("x1", fontsize=15)
ax.set_ylabel("x2", fontsize=15)
ax.tick_params(labelsize=15)

fig.tight_layout()
plt.show()
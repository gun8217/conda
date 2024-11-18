import numpy as np
import matplotlib.pyplot as plt

class Model:
    def __init__(self):
        rng = np.random.default_rng()
        self.w = rng.normal(0, 1, 1)
        self.b = rng.normal(0, 1, 1)
        
    def forward(self, x):
        self.x = x
        z = self.w * self.x + self.b
        return z
    
    def backward(self, dJ_dz, lr):
        dz_dw = self.x
        dz_db = 1
        
        dJ_dw = dJ_dz * dz_dw
        dJ_db = dJ_dz * dz_db
        
        self.w = self.w - lr * dJ_dw
        self.b = self.b - lr * dJ_db
    
    def get_params(self): return self.w, self.b


class SELoss:
    def forward(self, y, pred):
        self.y, self.pred = y, pred
        J = (y - pred)**2
        return J
    
    def backward(self):
        dJ_dpred = -2 * (self.y - self.pred)
        return dJ_dpred

    
n_data = 100
w_t, b_t = 2, 1

rng = np.random.default_rng(0)
x = rng.normal(0, 1, n_data)
noise = rng.normal(0, 1, n_data)
y = w_t * x + b_t + 0.1 * noise # y = wx + noise

fig, ax = plt.subplots(dpi=200)
ax.scatter(x, y, alpha=0.5)

model = Model()
loss_function = SELoss()

x_model = np.array(ax.get_xlim())
w, b = model.get_params()
y_model = x_model * w + b
cmap = plt.colormaps['rainbow']
colors = cmap(np.linspace(0, 1, len(x)))
ax.plot(x_model, y_model, color=colors[0], lw=3)

lr = 0.02
for data_idx, (x_, y_) in enumerate(zip(x, y)):
    pred = model.forward(x_)
    J = loss_function.forward(y_, pred)
    dJ_dpred = loss_function.backward()
    model.backward(dJ_dpred, lr)
    w, b = model.get_params()
    y_model = x_model * w + b
    ax.plot(x_model, y_model, color=colors[data_idx], alpha=0.3)
    
ax.axhline(y=0, color='gray', lw=0.5, ls='--')
ax.axvline(x=0, color='gray', lw=0.5, ls='--')

plt.tight_layout()
plt.show()
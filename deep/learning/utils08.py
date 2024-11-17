import numpy as np

class AffineFunction:
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

class Sigmoid:    
    def forward(self, z):
        self.a = 1 / (1 + np.exp(-z))
        return self.a
    
    def backward(self, dJ_dpred):
        da_dz = self.a * (1 - self.a)
        dJ_dz = dJ_dpred * da_dz
        return dJ_dz

class BCELoss:
    def forward(self, y, pred):
        self.y, self.pred = y, pred
        J = -(y * np.log(pred) + (1 - y)*np.log(1 - pred))
        return J
    
    def backward(self):
        dJ_dpred = (self.pred - self.y) / (self.pred * (1 - self.pred))
        return dJ_dpred

class Model:
    def __init__(self):
        self.affine = AffineFunction()
        self.activation = Sigmoid()
        
    def forward(self, x):
        z = self.affine.forward(x)
        pred = self.activation.forward(z)
        return pred
    
    def backward(self, dJ_dpred, lr):
        dJ_dz = self.activation.backward(dJ_dpred)
        self.affine.backward(dJ_dz, lr)
import numpy as np

class AffineFunction:
    def __init__(self, w, b):
        self.w = w
        self.b = b
        
    def forword(self, x):
        z = np.dot(self.w, x) + self.b
        return z

class Sigmoid:
    def forword(self, z):
        a = 1 / (1 + np.exp(-z))
        return a
    
class ArtificialNeuron:
    def __init__(self, w, b):
        self.affine = AffineFunction(w=w, b=b)
        self.activation = Sigmoid()
    
    def forword(self, x):
        z = self.affine.forword(x)
        a = self.activation.forword(z)
        return a
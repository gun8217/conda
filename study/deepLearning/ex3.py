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
    
class XOR_Gate:
    def __init__(self):
        self.NAND = ArtificialNeuron(w=np.array([-5, -5]), b=7.5)
        self.OR = ArtificialNeuron(w=np.array([5, 5]), b=-2.5)
        self.AND = ArtificialNeuron(w=np.array([5, 5]), b=-7.5)

    def forword(self, x):
        a1 = self.NAND.forword(x)
        a2 = self.OR.forword(x)
        a = self.AND.forword([a1, a2])
        return a


XOR = XOR_Gate()
print(f"(0, 0): {XOR.forword(x=[0, 0]):.5f}")
print(f"(0, 1): {XOR.forword(x=[0, 1]):.5f}")
print(f"(1, 0): {XOR.forword(x=[1, 0]):.5f}")
print(f"(1, 1): {XOR.forword(x=[1, 1]):.5f}")
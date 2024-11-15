from utils import *

class Model:
    def __init__(self):
        self.NAND = ArtificialNeuron(w=np.array([-5, -5]), b=7.5)
        self.OR = ArtificialNeuron(w=np.array([5, 5]), b=-2.5)
        self.AND = ArtificialNeuron(w=np.array([5, 5]), b=-7.5)

    def forword(self, x):
        a1 = self.NAND.forword(x)
        a2 = self.OR.forword(x)
        a3 = self.AND.forword(x)
        
        a = np.array([a1, a2, a3])
        return a


model = Model()
print(f"(0, 0): {model.forword(x=[0, 0]):.5f}")
print(f"(0, 1): {model.forword(x=[0, 1]):.5f}")
print(f"(1, 0): {model.forword(x=[1, 0]):.5f}")
print(f"(1, 1): {model.forword(x=[1, 1]):.5f}")
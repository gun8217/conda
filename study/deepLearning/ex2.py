import numpy as np

class AffineFunction:
    def __init__(self, w, b):
        self.w = w  # 가중치
        self.b = b  # 편향
        
    def get_w(self):
        return self.w  # 가중치 반환

    def get_b(self):
        return self.b  # 편향 반환
    
    def forward(self, x):
        z = np.dot(self.w, x) + self.b
        return z
    
    # 행렬일 경우
    # def forward(self, X):
    #     X = np.array(X)  # 입력 행렬을 numpy 배열로 변환
    #     z = self.w @ X + self.b
    #     return z

affine1 = AffineFunction(w=[1, 1], b=-1.5)
affine2 = AffineFunction(w=[-1, -1], b=0.5)
print(affine1.get_w(), affine1.get_b())
print(affine2.get_w(), affine2.get_b())

x = [2, 3]
output1 = affine1.forward(x)
print("Output:", output1)
output2 = affine2.forward(x)
print("Output:", output2)
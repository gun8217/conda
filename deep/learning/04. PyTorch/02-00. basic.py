# PyTorch의 nn 모듈을 임포트
import torch.nn as nn

# Model 클래스는 nn.Module을 상속받음
# Model이 신경망의 레이어와 연산을 관리하는 PyTorch의 표준 방법을 따름
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        
    def forward(self, x):
        pass
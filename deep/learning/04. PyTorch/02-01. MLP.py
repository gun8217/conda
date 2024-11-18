# 퍼셉트론(Multi-Layer Perceptron, MLP)
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        
        # 3개의 선형 계층과 각 계층에 적용될 활성화 함수(Sigmoid) 정의
        # nn.Linear : 완전 연결 계층 정의
        # nn.Sigmoid : Sigmoid 활성화 함수 정의
        self.fc1 = nn.Linear(in_features=10, out_features=5)    # 1번째 선형 계층
        self.fc1_act = nn.Sigmoid()                             # 1번째 활성화 함수

        self.fc2 = nn.Linear(in_features=5, out_features=2)
        self.fc2_act = nn.Sigmoid()

        self.fc3 = nn.Linear(in_features=2, out_features=1)
        self.fc3_act = nn.Sigmoid()
        
    def forward(self, x):
        # 입력 데이터를 순차적으로 각 계층에 통과 : 각 계층을 거친 후 활성화 함수 적용
        x = self.fc1(x)
        x = self.fc1_act(x)

        x = self.fc2(x)
        x = self.fc2_act(x)

        x = self.fc3(x)
        x = self.fc3_act(x)
        return x
    

import torch

# 32 : data, 10 : features
test_input = torch.randn(size=(32, 10))

# MLP 모델 생성
model = MLP()

# 입력 데이터를 모델에 통과시켜 예측값 계산
test_output = model(test_input)


print(f"test input: {test_input.shape}")
print(f"test output: {test_output.shape}")
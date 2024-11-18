# 분류 모델을 만들 때 마지막 레이어는 nn.Linear로 끝나는 것이 일반적

# 이진 분류 (Binary Classification):
# 마지막 레이어: nn.Linear(out_features=1)
# 손실 함수: nn.BCEWithLogitsLoss() (또는 nn.CrossEntropyLoss()와 함께 out_features=2 사용)

# 다중 클래스 분류 (Multiclass Classification):
# 마지막 레이어: nn.Linear(out_features=클래스 수)
# 손실 함수: nn.CrossEntropyLoss()

import torch
import torch.nn as nn

class Classifier(nn.Module):
    def __init__(self):
        super(Classifier, self).__init__()
        
        self.fc1 = nn.Linear(in_features=10, out_features=16)
        self.fc1_act = nn.ReLU()
        
        self.fc2 = nn.Linear(in_features=16, out_features=32)
        self.fc2_act = nn.ReLU()
        
        self.fc3 = nn.Linear(in_features=32, out_features=10)
        
    def forward(self, x):
        x = self.fc1(x)
        x = self.fc1_act(x)
        
        x = self.fc2(x)
        x = self.fc2_act(x)
        
        x = self.fc3(x)
        return x

# model과 nn.CrossEntropyLoss 만들기
model = Classifier()
loss_function = nn.CrossEntropyLoss()

# 입력 데이터 (크기를 (1, 10)으로 설정)
input_data = torch.randn(1, 10)
labels = torch.tensor([0])  # 실제 레이블

preds = model(input_data)
loss = loss_function(preds, labels)

print(f'손실 값: {loss.item()}')
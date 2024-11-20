import torch.nn as nn

# 5개의 클래스를 예측하는 모델을 가정
class Classifier(nn.Module):
    def __init__(self):
        super(Classifier, self).__init__()
        self.fc1 = nn.Linear(in_features=10, out_features=16)
        self.fc1_act = nn.ReLU()
        
        self.fc2 = nn.Linear(in_features=16, out_features=32)
        self.fc2_act = nn.ReLU()
        
        self.fc3 = nn.Linear(in_features=32, out_features=5)
        
    def forward(self, x):
        x = self.fc1(x)
        x = self.fc1_act(x)
        
        x = self.fc2(x)
        x = self.fc2_act(x)
        
        x = self.fc3(x)
        return x


import torch

BATCH_SIZE = 4
N_FEATURES = 10

model = Classifier()
test_input = torch.randn(size=(BATCH_SIZE, N_FEATURES))
preds = model(test_input)

# 4개 샘플에 대해 5개의 확률벡터를 출력하기 때문에 출력은 (4, 5)의 shape을 가짐
print(preds.shape) # torch.Size([4, 5])

print(f"preds:\n{preds}")
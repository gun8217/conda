import torch.nn as nn


class Classifier(nn.Module):
    def __init__(self):
        super(Classifier, self).__init__()
        
        self.fc1 = nn.Linear(in_features=10, out_features=16)
        self.fc1_act = nn.ReLU()
        
        self.fc2 = nn.Linear(in_features=16, out_features=32)
        self.fc2_act = nn.ReLU()
        
        self.fc3 = nn.Linear(in_features=32, out_features=10)
        # 소프트맥스 : 확률 분포 계산
        # dim=1: 각 데이터 샘플(행)에 대해 클래스별 확률 계산 (일반적으로 분류 문제에서 사용)
        # dim=0: 각 클래스(열)에 대해 배치 전체의 확률 계산 (특정 상황에서만 사용)
        # dim=0: 서로 다른 클래스 간의 확률 분포를 비교
        # dim=0: 특정 작업에서 배치 차원이 아닌 다른 차원을 기준으로 소프트맥스를 적용해야 할 때 사용
        self.softmax = nn.Softmax(dim=1)
        
    def forward(self, x):
        x = self.fc1(x)
        x = self.fc1_act(x)
        
        x = self.fc2(x)
        x = self.fc2_act(x)
        
        x = self.fc3(x)
        # 출력 값을 확률로 변환
        x = self.softmax(x)
        return x
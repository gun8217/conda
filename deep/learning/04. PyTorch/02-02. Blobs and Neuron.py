import torch
import numpy as np
import torch.nn as nn
from sklearn.datasets import make_blobs
from torch.utils.data import TensorDataset, DataLoader

# 랜덤 시드 설정
torch.manual_seed(0)
np.random.seed(0)


class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        
        # artificial neuron 하나만 만들기 : make_blobs는 직선으로 나눌 수 있으므로        
        self.fc = nn.Linear(in_features=2, out_features=1)
        # binary classification이므로 sigmoid
        self.fc_act = nn.Sigmoid()
        
    def forward(self, x):
        x = self.fc(x)
        x = self.fc_act(x)
        
        # 이진 분류법 : 반드시 최종 값이 단일 값이여야 함
        # (B, 1)을 (B, )의 벡터로 만들어주기
        x = x.view(-1)
        return x


N_SAMPLES = 100
BATCH_SIZE = 8

# make_blobs를 사용하여 클러스터링된 데이터를 생성
X, y = make_blobs(n_samples=N_SAMPLES, centers=2, n_features=2, cluster_std=0.5, random_state=0)

# PyTorch의 Dataset 객체 만들기 : float형 텐서로 변환
dataset = TensorDataset(torch.FloatTensor(X), torch.FloatTensor(y))
# DataLoader를 사용하여 데이터셋을 배치 단위 로드
data_loader = DataLoader(dataset=dataset, batch_size=BATCH_SIZE)

for X_batch, y_batch in data_loader:
    print(type(X_batch), X_batch.shape, X_batch.dtype)
    print(type(y_batch), y_batch.shape, y_batch.dtype)
    break



# 확률적 경사 하강법(Stochastic Gradient Descent)을 사용하여 모델을 학습시키기 위한 최적화 알고리즘
from torch.optim import SGD

LR = 0.1

if torch.cuda.is_available(): DEVICE = 'cuda'               # NVIDIA GPU가 사용 가능하면 DEVICE는 'cuda'
elif torch.backends.mps.is_available(): DEVICE = 'mps'      # Mac의 GPU가 사용 가능하면 DEVICE는 'mps'
else: DEVICE = 'cpu'                                        # 그 외에는 DEVICE는 'cpu'

# 모델
model = SimpleModel().to(DEVICE)
# 손실 함수(BCE)
loss_function = nn.BCELoss()
# 최적화 알고리즘
optimizer = SGD(model.parameters(), lr=LR)


# 손실 값을 저장할 리스트
losses = []

EPOCHS = 10
# 데이터셋을 10번 반복해서 학습할 것
for epoch in range(EPOCHS):
    # 전체 Loss : 기본 선언
    epoch_loss = 0.
    for X, y in data_loader:
        # 데이터를 DEVICE로 옮기기
        X, y = X.to(DEVICE), y.to(DEVICE)
        
        # 순전파
        pred = model(X)
        # 손실 계산
        loss = loss_function(pred, y)
        # 기울기 초기화
        optimizer.zero_grad()
        # 역전파
        loss.backward()                                      # 모델의 parameter가 학습되는 부분
        # 가중치 업데이트
        optimizer.step()
        
        # 전체 Loss : Batch size의 loss로 변환하여 누적
        epoch_loss += loss.item() * len(X)
        
    # 전체 Loss : 데이터셋의 전체 개수로 누적된 loss를 나눠줌
    epoch_loss /= N_SAMPLES
    
    # 에폭 당 평균 손실값 계산
    epoch_loss /= len(data_loader)
    losses.append(epoch_loss)
        
    # 각 epoch이 완료될 때마다 epoch 번호 출력
    print(f"Epoch: {epoch + 1}")
    # 전체 Loss 출력
    print(f"Loss: {epoch_loss:.4f}\n")



import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 3))
ax.plot(losses)
ax.set_xlabel("Epoch", fontsize=15)
ax.set_ylabel("BCE Loss", fontsize=15)
ax.tick_params(labelsize=10)

fig.tight_layout()
plt.show()
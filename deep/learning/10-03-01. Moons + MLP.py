from sklearn.datasets import make_moons

import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
from torch.optim import SGD

# 학습 변수 설정
N_SAMPLES = 300
BATCH_SIZE = 8
LR = 0.01
EPOCHS = 100

if torch.cuda.is_available(): DEVICE = 'cuda'
elif torch.backends.mps.is_available(): DEVICE = 'mps'
else: DEVICE = 'cpu'


# 데이터셋 준비
X, y = make_moons(n_samples=N_SAMPLES, noise=0.2)
dataset = TensorDataset(torch.FloatTensor(X), torch.FloatTensor(y))
dataloader = DataLoader(dataset=dataset, batch_size=BATCH_SIZE)


# 모델 만들기
class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        
        self.fc1 = nn.Linear(in_features=2, out_features=32)
        self.fc1_act = nn.ReLU()
        
        self.fc2 = nn.Linear(in_features=32, out_features=16)
        self.fc2_act = nn.ReLU()
        
        self.fc3 = nn.Linear(in_features=16, out_features=1)
        self.fc3_act = nn.Sigmoid()
        
    def forward(self, x):
        x = self.fc1(x)
        x = self.fc1_act(x)
        
        x = self.fc2(x)
        x = self.fc2_act(x)
        
        x = self.fc3(x)
        x = self.fc3_act(x)
        
        x = x.view(-1)
        return x


# 학습 Object 만들기
model = MLP().to(DEVICE)
loss_function = nn.BCELoss()
optimizer = SGD(model.parameters(), lr=LR)


# 학습시키기
losses, accs = [], []
for epoch in range(EPOCHS):
    epoch_loss, n_corrects = 0., 0
    for X_, y_ in dataloader:
        X_, y_ = X_.to(DEVICE), y_.to(DEVICE)
        
        pred = model(X_)
        loss = loss_function(pred, y_)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        epoch_loss += loss.item() * len(X_)
        pred = (pred > 0.5)
        n_corrects += (pred == y_).sum().item()
        
    epoch_loss /= N_SAMPLES
    losses.append(epoch_loss)
    epoch_acc = n_corrects / N_SAMPLES
    accs.append(epoch_acc)
    
    print(f"Epoch: {epoch + 1}")
    print(f"Loss: {epoch_loss:.4f} - Acc: {epoch_acc:.4f}\n")


# 결과 시각화하기
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 1, figsize=(10, 5))

axes[0].plot(losses)
axes[0].set_ylabel("BCE Loss", fontsize=15)
axes[0].tick_params(labelsize=10)

axes[1].plot(accs)
axes[1].set_xlabel("Epoch", fontsize=15)
axes[1].set_ylabel("Accuracy", fontsize=15)
axes[1].tick_params(labelsize=10)

fig.tight_layout()
plt.show()
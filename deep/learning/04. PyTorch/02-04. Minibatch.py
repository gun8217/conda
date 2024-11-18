import torch
import numpy as np
import torch.nn as nn
from sklearn.datasets import make_blobs
from torch.utils.data import TensorDataset, DataLoader

torch.manual_seed(0)
np.random.seed(0)


class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
            
        self.fc = nn.Linear(in_features=2, out_features=1)
        self.fc_act = nn.Sigmoid()
        
    def forward(self, x):
        x = self.fc(x)
        x = self.fc_act(x)        
        x = x.view(-1)
        return x


N_SAMPLES = 100
BATCH_SIZE = 8

X, y = make_blobs(n_samples=N_SAMPLES, centers=2, n_features=2, cluster_std=0.5, random_state=0)

dataset = TensorDataset(torch.FloatTensor(X), torch.FloatTensor(y))
data_loader = DataLoader(dataset=dataset, batch_size=BATCH_SIZE)


from torch.optim import SGD

LR = 0.1

if torch.cuda.is_available(): DEVICE = 'cuda'
elif torch.backends.mps.is_available(): DEVICE = 'mps'
else: DEVICE = 'cpu'

model = SimpleModel().to(DEVICE)
loss_function = nn.BCELoss()
optimizer = SGD(model.parameters(), lr=LR)


EPOCHS = 10
for epoch in range(EPOCHS):
    for X, y in data_loader:
        X, y = X.to(DEVICE), y.to(DEVICE)
        
        pred = model(X)
        loss = loss_function(pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
                
        pred = (pred > 0.5)
        # 정답과 동일한지 연산
        is_proper_preds = (pred == y)
        # 정답과 동일한 개수 구하기
        n_corrects = is_proper_preds.sum().item()
        print(is_proper_preds)
        print(f"{n_corrects = }\n")
        
        break

# 성능 발전 과정 확인
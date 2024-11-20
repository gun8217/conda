from sklearn.datasets import make_blobs
from torch import FloatTensor, LongTensor
from torch.utils.data import TensorDataset, DataLoader

import torch
import torch.nn as nn
from torch.optim import SGD

from model04 import MLP

n_samples = 100
n_classes = 4
batch_size = 8

X, y = make_blobs(n_samples=n_samples, centers=n_classes,
                  n_features=2, cluster_std=0.7, random_state=1)

dataset = TensorDataset(FloatTensor(X), LongTensor(y))
dataloader = DataLoader(dataset, batch_size=batch_size)

BATCH_SIZE = 8
LR = 0.01
EPOCHS = 100

if torch.cuda.is_available(): DEVICE = 'cuda'
elif torch.backends.mps.is_available(): DEVICE = 'mps'
else: DEVICE = 'cpu'

model = MLP().to(DEVICE)
loss_function = nn.CrossEntropyLoss()
optimizer = SGD(model.parameters(), lr=LR)

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
        n_corrects += (torch.max(pred, axis=1)[1] == y_).sum().item()
        
    # 에포크 별 평균 손실 값 계산
    epoch_loss /= n_samples
    losses.append(epoch_loss)
    
    epoch_acc = n_corrects / n_samples
    accs.append(epoch_acc)
    
    print(f"Epoch: {epoch + 1}")
    print(f"Loss: {epoch_loss:.4f} - Acc: {epoch_acc:.4f}")

import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 1, figsize=(10, 5))

axes[0].plot(losses)
axes[0].set_ylabel("Cross Entropy Loss", fontsize=15)
axes[0].tick_params(labelsize=10)

axes[1].plot(accs)
axes[1].set_xlabel("Epoch", fontsize=15)
axes[1].set_ylabel("Accuracy", fontsize=15)
axes[1].tick_params(labelsize=10)

fig.tight_layout()
plt.show()



fig, ax = plt.subplots(figsize=(10, 10))
colors = ['red', 'green', 'blue', 'purple']

for class_idx in range(n_classes):
    class_X = X[y == class_idx]
    ax.scatter(class_X[:, 0], class_X[:, 1], color=colors[class_idx])
    
xlim, ylim = ax.get_xlim(), ax.get_ylim()
x1 = torch.linspace(xlim[0], xlim[1], 100)
x2 = torch.linspace(ylim[0], ylim[1], 100)
X1, X2 = torch.meshgrid(x1, x2)

X_db = torch.hstack([X1.reshape(-1, 1), X2.reshape(-1, 1)]).to(DEVICE)
y_db = model(X_db)
y_db = torch.max(y_db, axis=1)[1]

X_db = X_db.cpu().numpy()
y_db = y_db.cpu().detach().numpy()

for class_idx in range(n_classes):
    class_X_db = X_db[y_db == class_idx]
    ax.scatter(class_X_db[:, 0], class_X_db[:, 1], color=colors[class_idx], alpha=0.1)
    
plt.show()
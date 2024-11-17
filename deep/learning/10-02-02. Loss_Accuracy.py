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
losses, accs = [], []
for epoch in range(EPOCHS):
    epoch_loss, n_corrects = 0., 0
    for X, y in data_loader:
        X, y = X.to(DEVICE), y.to(DEVICE)
        
        pred = model(X)
        loss = loss_function(pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        epoch_loss += loss.item() * len(X)
        pred = (pred > 0.5)
        n_corrects += (pred == y).sum().item()
        
    epoch_loss /= N_SAMPLES
    losses.append(epoch_loss)
    epoch_acc = n_corrects / N_SAMPLES
    accs.append(epoch_acc)
    
    print(f"Epoch: {epoch + 1}")
    print(f"Loss: {epoch_loss:.4f} - Acc: {epoch_acc:.4f}\n")



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
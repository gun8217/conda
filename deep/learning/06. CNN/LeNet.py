from tqdm import tqdm
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torch.optim import SGD
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor

BATCH_SIZE = 32
LR = 0.1
EPOCHS = 5

if torch.cuda.is_available(): DEVICE = 'cuda'
elif torch.backends.mps.is_available(): DEVICE = 'mps'
else: DEVICE = 'cpu'


from LeNet_model import LeNet

train_ds = MNIST(root='data', train=True, download=True, transform=ToTensor())
n_train_samples = len(train_ds)
train_loader = DataLoader(dataset=train_ds, batch_size=BATCH_SIZE, shuffle=True)

model = LeNet().to(DEVICE)
loss_fn = nn.CrossEntropyLoss()
optimizer = SGD(model.parameters(), lr=LR)

losses, accs = [], []
for epoch in range(EPOCHS):
    loss_epoch, n_corrects = 0., 0
    for imgs, labels in tqdm(train_loader):
        imgs, labels = imgs.to(DEVICE), labels.to(DEVICE)
        preds = model(imgs)

        loss = loss_fn(preds, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        n_samples = imgs.shape[0]
        loss_epoch += loss.item() * n_samples
        _, pred_classes = torch.max(preds, axis=1)
        n_corrects += torch.sum(pred_classes == labels).item()
    
    loss_epoch /= n_train_samples
    acc_epoch = n_corrects / n_train_samples

    losses.append(loss_epoch)
    accs.append(acc_epoch)

    print(f"\nEpoch: {epoch + 1}")
    print(f"Train Loss: {loss_epoch:.4f}, Train Acc: {acc_epoch:.4f}\n")

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
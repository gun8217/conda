from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader

BATCH_SIZE = 32
dataset = MNIST(root='data', train=True, download=True, transform=ToTensor())
dataloader = DataLoader(dataset, batch_size=BATCH_SIZE)
n_samples = len(dataset)

from model06 import MNIST_Classifier

import torch
import torch.nn as nn
from tqdm import tqdm
from torch.optim import SGD

LR = 0.003
EPOCHS = 10

if torch.cuda.is_available(): DEVICE = 'cuda'
elif torch.backends.mps.is_available(): DEVICE = 'mps'
else: DEVICE = 'cpu'

model = MNIST_Classifier().to(DEVICE)
loss_function = nn.CrossEntropyLoss()
optimizer = SGD(model.parameters(), lr=LR)

losses, accs = [], []
for epoch in range(EPOCHS):
    epoch_loss, n_corrects = 0., 0
    for X_, y_ in tqdm(dataloader):
        X_, y_ = X_.to(DEVICE), y_.to(DEVICE)
        X_ = X_.reshape(BATCH_SIZE, -1)
        
        pred = model(X_)
        loss = loss_function(pred, y_)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        epoch_loss += loss.item() * len(X_)
        n_corrects += (torch.max(pred, axis=1)[1] == y_).sum().item()
        
    epoch_loss /= n_samples
    losses.append(epoch_loss)
    
    epoch_acc = n_corrects / n_samples
    accs.append(epoch_acc)
    
    print(f"Epoch: {epoch + 1}")
    print(f"Loss: {epoch_loss:.4f} - Acc: {epoch_acc:.4f}")
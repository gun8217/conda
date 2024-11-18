from utils import get_dataset, get_device, train, vis_losses_accs
from model import MLP

import torch.nn as nn
from torch.optim import SGD

N_SAMPLES = 300
BATCH_SIZE = 8
EPOCHS = 100
LR = 0.01
DEVICE = get_device()

dataloader = get_dataset(N_SAMPLES, BATCH_SIZE)

model = MLP().to(DEVICE)
loss_function = nn.BCELoss()
optimizer = SGD(model.parameters(), lr=LR)

losses, accs = [], []
for epoch in range(EPOCHS):
    epoch_loss, epoch_acc = train(dataloader, N_SAMPLES, model, loss_function, optimizer, DEVICE)
    
    losses.append(epoch_loss)
    accs.append(epoch_acc)
    
    print(f"Epoch: {epoch + 1}")
    print(f"Loss: {epoch_loss:.4f} - Acc: {epoch_acc:.4f}\n")

vis_losses_accs(losses, accs)
import torch
from torch.utils.data import TensorDataset, DataLoader

import matplotlib.pyplot as plt

from sklearn.datasets import make_moons


def get_dataset(n_samples, batch_size):
    X, y = make_moons(n_samples=n_samples, noise=0.2)
    dataset = TensorDataset(torch.FloatTensor(X), torch.FloatTensor(y))
    data_loader = DataLoader(dataset=dataset, batch_size=batch_size)
    return data_loader


def get_device():
    if torch.cuda.is_available(): device = 'cuda'
    elif torch.backends.mps.is_available(): device = 'mps'
    else: device = 'cpu'
    return device


def train(dataloader, n_samples, model, loss_function, optimizer, device):
    epoch_loss, n_corrects = 0., 0
    for X, y in dataloader:
        X, y = X.to(device), y.to(device)
        
        pred = model(X)
        loss = loss_function(pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
            
        epoch_loss += loss.item() * len(X)
        pred = (pred > 0.5)
        n_corrects += (pred == y).sum().item()

    epoch_loss /= n_samples
    epoch_acc = n_corrects / n_samples
    return epoch_loss, epoch_acc


def vis_losses_accs(losses, accs):
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
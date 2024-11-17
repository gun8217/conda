from sklearn.datasets import make_moons
import torch
from torch.utils.data import TensorDataset, DataLoader

n_samples = 300
BATCH_SIZE = 16

X, y = make_moons(n_samples=n_samples, noise=0.2)

dataset = TensorDataset(torch.FloatTensor(X), torch.FloatTensor(y))

dataloader = DataLoader(dataset, batch_size=BATCH_SIZE)
for X_, y_ in dataloader:
    print(type(X_), X_.shape, X_.dtype)
    print(type(y_), y_.shape, y_.dtype)
    break
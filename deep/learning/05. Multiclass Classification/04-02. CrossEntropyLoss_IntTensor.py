from sklearn.datasets import make_blobs
from torch import FloatTensor, IntTensor  # IntTensor : torch.int32
from torch.utils.data import TensorDataset, DataLoader

n_samples = 100
n_classes = 4
batch_size = 8

X, y = make_blobs(n_samples=n_samples, centers=n_classes,
                  n_features=2, cluster_std=0.7, random_state=1)

dataset = TensorDataset(FloatTensor(X), IntTensor(y))
dataloader = DataLoader(dataset, batch_size=batch_size)
import numpy as np
from torchvision.datasets import MNIST

dataset = MNIST(root='data', train=True, download=True)

for img, label in dataset:
    img = np.array(img) 
    print(img.shape, img.dtype)
    break

# (28, 28)의 이미지가 uint8로 들어있는 것을 알 수 있음
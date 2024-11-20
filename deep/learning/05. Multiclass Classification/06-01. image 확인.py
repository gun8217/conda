from torchvision.datasets import MNIST

dataset = MNIST(root='data', train=True, download=True)

for img, label in dataset:
    img.show()
    print(type(label)) # <class 'int'>
    break

# NOTE: 이 이미지를 다룰 때 PIL.Image를 그대로 사용하지 않고,
# PyTorch의 Tensor나 NumPy의 ndarray로 바꿔서 사용함
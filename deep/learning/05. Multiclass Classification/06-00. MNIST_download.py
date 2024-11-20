from torchvision.datasets import MNIST

dataset = MNIST(root='data', train=True, download=True)

for img, label in dataset:
    print(type(img)) # <class 'PIL.Image.Image'>
    print(type(label)) # <class 'int'>
    break
import torch.nn as nn

class MNIST_Classifier(nn.Module):
    def __init__(self):
        super(MNIST_Classifier, self).__init__()
        self.fc1 = nn.Linear(in_features=784, out_features=512)
        self.fc1_act = nn.ReLU()
        
        self.fc2 = nn.Linear(in_features=512, out_features=128)
        self.fc2_act = nn.ReLU()
        
        self.fc3 = nn.Linear(in_features=128, out_features=52)
        self.fc3_act = nn.ReLU()
        
        self.fc4 = nn.Linear(in_features=52, out_features=10)
        
    def forward(self, x):
        x = self.fc1_act(self.fc1(x))
        
        x = self.fc2_act(self.fc2(x))
        
        x = self.fc3_act(self.fc3(x))
        
        x = self.fc4(x)
        return x
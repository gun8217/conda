import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split

# 데이터셋 생성
N_SAMPLES = 400
centers = [(1, -1), (-1, 1), (-1, -1), (1, 1)]
X, y = make_blobs(n_samples=N_SAMPLES, centers=centers, cluster_std=0.2)
y = np.where(y < 2, 0, 1)

# 데이터셋을 Tensor로 변환
X_tensor = torch.FloatTensor(X)
y_tensor = torch.LongTensor(y)

# 학습용 데이터와 검증용 데이터로 분리
X_train, X_val, y_train, y_val = train_test_split(X_tensor, y_tensor, test_size=0.2, random_state=42)

# 간단한 신경망 모델 정의
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(2, 10)
        self.fc2 = nn.Linear(10, 2)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 모델, 손실 함수, 최적화 알고리즘 정의
model = SimpleNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.05)

# 학습 함수 정의
def train(model, criterion, optimizer, X_train, y_train, X_val, y_val, epochs=100):
    train_losses = []
    val_accuracies = []
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()
        
        train_losses.append(loss.item())
        
        model.eval()
        with torch.no_grad():
            outputs_val = model(X_val)
            _, predicted = torch.max(outputs_val.data, 1)
            accuracy = (predicted == y_val).sum().item() / y_val.size(0)
            val_accuracies.append(accuracy)
        
        if (epoch + 1) % 10 == 0:
            print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}, Validation Accuracy: {accuracy:.4f}')
    
    return train_losses, val_accuracies

# 모델 학습
train_losses, val_accuracies = train(model, criterion, optimizer, X_train, y_train, X_val, y_val)

# 결정 경계 시각화 함수
def plot_decision_boundary(model, X, y):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
    X_grid = torch.FloatTensor(np.c_[xx.ravel(), yy.ravel()])
    with torch.no_grad():
        Z = model(X_grid)
        _, Z = torch.max(Z, 1)
        Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Decision Boundary')

# 결정 경계 그리기
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plot_decision_boundary(model, X, y)

# 학습 손실 및 검증 정확도 그래프 그리기
epochs = range(100)
plt.subplot(1, 2, 2)
plt.plot(epochs, train_losses, label='Loss')
plt.plot(epochs, val_accuracies, label='Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Value')
plt.legend()

plt.tight_layout()
plt.show()
from sklearn.datasets import make_blobs
import torch
from torch.utils.data import TensorDataset, DataLoader

n_samples = 100

# X : 입력 데이터 (feature), y : 해당 데이터에 대한 레이블
X, y = make_blobs(n_samples=n_samples, centers=2, n_features=2, cluster_std=0.7)

# 텐서 형식의 입력과 레이블을 받아서 데이터셋 생성
# X 데이터를 float형 텐서로 변환
# y 데이터를 float형 텐서로 변환
dataset = TensorDataset(torch.FloatTensor(X), torch.FloatTensor(y))

# 한 번에 처리할 데이터의 개수 지정
BATCH_SIZE = 8

# 주어진 데이터셋을 배치 단위로 로드
dataloader = DataLoader(dataset, batch_size=BATCH_SIZE)

# DataLoader에서 배치 단위로 데이터를 로드
for X_, y_ in dataloader:
    # 각 배치의 입력 데이터 X_와 레이블 y_의 타입, 크기(shape), 데이터 타입(dtype)을 출력
    print(type(X_), X_.shape, X_.dtype)
    print(type(y_), y_.shape, y_.dtype)
    
    # 첫 번째 배치만 출력
    break
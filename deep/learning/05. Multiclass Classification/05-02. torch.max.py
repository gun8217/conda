import torch

BATCH_SIZE = 4
N_CLASSES = 5

preds = torch.randn(size=(BATCH_SIZE, N_CLASSES))
labels = torch.tensor([4, 0, 1, 3])
print(f"preds:\n{preds}")

# torch.max는 axis=1을 기준으로 최댓값, 최댓값의 index 계산
pred_classes = torch.max(preds, axis=1)
print(f"pred_classes:\n{pred_classes}")

# 각 데이터 샘플의 최댓값 (각 샘플의 최댓값 확률)
pred_classes0 = torch.max(preds, axis=1)[0]
print(f"pred_classes0:\n{pred_classes0}")

# 각 데이터 샘플의 최댓값 인덱스 (각 샘플의 예측 클래스)
pred_classes1 = torch.max(preds, axis=1)[1]
print(f"pred_classes1:\n{pred_classes1}")
print(f"labels: {labels}")

n_corrects = (pred_classes1 == labels).sum()
print(f"n corrects: {n_corrects}")
# 이진 분류 : 전체 예측 중에서 올바르게 분류된 샘플의 비율(정확도)

import random

n_data = 100
preds = [random.randint(0, 1) for _ in range(n_data)]
labels = [random.randint(0, 1) for _ in range(n_data)]
print(f"{preds = }")
print(f"{labels = }\n")

n_corrects = 0
for p, l in zip(preds, labels):
    if p == l: # 예측(p)과 실제 레이블(l)이 일치하면 정확한 예측으로 간주
        n_corrects += 1 # 정확한 예측은 1 증가
acc = n_corrects / n_data # 전체 데이터의 수로 정확한 예측의 수를 나누어 정확도 계산
print(f"{acc = :.2f}")
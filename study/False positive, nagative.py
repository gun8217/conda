# 모델 예측 기준 FP : positive -> negative, FN : negative - positive
# confution matrix

import random

n_data = 10
preds = [random.randint(0, 1) for _ in range(n_data)]
labels = [random.randint(0, 1) for _ in range(n_data)]
print(f"{preds = }")
print(f"{labels = }\n")

c_FP, c_FN = 0, 0
for p, l in zip(preds, labels):
    if p != l:
        if p == 1:
            c_FP += 1
        else:
            c_FN += 1
print(f"{c_FP = }")
print(f"{c_FN = }")

c_FP2, c_FN2 = 0, 0
for p, l in zip(preds, labels):
    if p != l and p == 1:
        c_FP2 += 1
    if p != l and p == 0:
        c_FN2 += 1

print(f"{c_FP2 = }")
print(f"{c_FN2 = }")
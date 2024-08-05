# True Positive (TP): Positive 클래스를 정확히 예측한 경우(긍정적인 클래스를 올바르게 식별한 수)
# True Negative (TN): Negative 클래스를 정확히 예측한 경우(부정적인 클래스를 올바르게 식별한 수)
# False Positive (FP): Positive 클래스를 잘못 예측한 경우(부정적인 클래스를 긍정적인 클래스로 잘못 분류한 수)
# False Negative (FN): Negative 클래스를 잘못 예측한 경우(긍정적인 클래스를 부정적인 클래스로 잘못 분류한 수)

import random

n_data = 100
preds = [random.randint(0, 1) for _ in range(n_data)]
labels = [random.randint(0, 1) for _ in range(n_data)]
print(f"{preds = }")
print(f"{labels = }\n")

# 혼동 행렬의 요소 계산 type1
TP = TN = FP = FN = 0
for pred, label in zip(preds, labels):
    if pred == 1 and label == 1:
        TP += 1
    elif pred == 0 and label == 0:
        TN += 1
    elif pred == 0 and label == 1:
        FP += 1
    elif pred == 1 and label == 0:
        FN += 1
print(f"{TP = }, {TN = }, {FP = }, {FN = }\n")

# 혼동 행렬의 요소 계산 type2
n_TP = n_TN = n_FP = n_FN = 0
for pred, label in zip(preds, labels):
    if pred == label:    
        if pred == 1 : n_TP += 1
        else: n_TN += 1
    else:
        if pred == 1 : n_FP += 1
        else: n_FN += 1

print(f"{n_TP = } | {n_FP = }\n")
print(f"{n_FN = } | {n_TN = }")
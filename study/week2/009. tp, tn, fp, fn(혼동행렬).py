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
TP1 = TN1 = FP1 = FN1 = 0
for pred, label in zip(preds, labels):
    if pred == 1 and label == 1:
        TP1 += 1
    elif pred == 0 and label == 0:
        TN1 += 1
    elif pred == 0 and label == 1:
        FP1 += 1
    elif pred == 1 and label == 0:
        FN1 += 1
print(f"{TP1 = }, {TN1 = }, {FP1 = }, {FN1 = }\n")

# 혼동 행렬의 요소 계산 type2
TP2 = TN2 = FP2 = FN2 = 0
for pred, label in zip(preds, labels):
    if pred == label:    
        if pred == 1 : TP2 += 1
        else: TN2 += 1
    else:
        if pred == 1 : FN2 += 1
        else: FP2 += 1

print(f"{TP2 = }, {TN2 = }, {FP2 = }, {FN2 = }\n")

# 혼동 행렬의 요소 계산 type3
TP3 = sum(1 for pred, label in zip(preds, labels) if pred == 1 and label == 1)
TN3 = sum(1 for pred, label in zip(preds, labels) if pred == 0 and label == 0)
FP3 = sum(1 for pred, label in zip(preds, labels) if pred == 0 and label == 1)
FN3 = sum(1 for pred, label in zip(preds, labels) if pred == 1 and label == 0)
print(f"{TP3 = }, {TN3 = }, {FP3 = }, {FN3 = }\n")
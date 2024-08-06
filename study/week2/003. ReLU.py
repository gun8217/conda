# ReLU(ativation 함수) : 양수-x, 음수-0
# 딥러닝 및 머신러닝에서 사용(비선형 함수, 신경망의 복잡성을 증가시키고 모델의 성능을 개선)
# 컨볼루션 신경망(CNN)과 다층 퍼셉트론(MLP)에서 사용
import random

num = int(input("ReLU : "))
if num > 0: relu = num
else: relu = 0
print(f"relu({num}) = {relu}")


######## ReLU 리스트 ###################################################
n_data = 5
data = [random.randint(-10, 10) for _ in range(n_data)]
print(f"{data}\n")

relu_values = []
for data_ in data:
    if data_ >= 0: relu_values.append(data_)
    else: relu_values.append(0)
print(relu_values)
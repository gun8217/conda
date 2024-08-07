import random


def relu(data):
    relu_values = []
    for sample in data:
        if sample >= 0: relu_values.append(sample)
        else: relu_values.append(0)
        return relu_values


n_data = 10
data = [round(random.uniform(-5, 5), 2) for _ in range(n_data)]
print(data)

relu_values = relu(data)
for sample, relu_value in zip(data, relu_values):
    print(f"{sample:15} -> {relu_value:5}")
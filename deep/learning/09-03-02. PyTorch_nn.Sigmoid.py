import torch
import torch.nn as nn

test_input = torch.randn(size=(2, 3))
sigmoid = nn.Sigmoid()
test_output = sigmoid(test_input)

print("===== Test Input =====")
print(test_input, '\n')
print("===== nn.Simgoid Output =====")
print(test_output, '\n')
print("===== Manual Computation =====")
print(1 / (1 + torch.exp(-test_input)))


# a = σ(z) = 1 / 1 + e−z
import torch
import torch.nn as nn

test_pred = torch.tensor([0.8])
test_y = torch.tensor([1.])
loss_function = nn.BCELoss()
test_output = loss_function(test_pred, test_y)

print("===== Test Input =====")
print("pred:", test_pred)
print("y:", test_y, '\n')
print("===== nn.BCELoss Output =====")
print(test_output, '\n')
print("===== Manual Computation =====")
print(-(test_y * torch.log(test_pred) + (1 - test_y) * torch.log(1 - test_pred)))


# J(y^, y)=-[ylog(y^) + (1 - y)log(1 - y^)]
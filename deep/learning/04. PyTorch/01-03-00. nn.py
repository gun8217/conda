import torch.nn as nn

# nn.Linear: fully connected layer
# in_features: 입력되는 feature의 개수
# out_features: 출력되는 feature의 개수
# 출력되는 feature의 개수는 곧 레이어가 가지는 뉴런의 개수

# 뉴런 하나는 8개의 weight와 1개의 bias를 가짐
# 레이어에는 4개의 뉴런이 존재
fc = nn.Linear(in_features=8, out_features=4)

# 출력 뉴런(4) × 입력 특성(8)
print(fc.weight.shape)
# 각 출력 뉴런마다 하나의 bais 추가 : bais 벡터(4)
print(fc.bias.shape)
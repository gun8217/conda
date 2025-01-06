import torch
import math

# x = torch.empty(3, 4)
# print(type(x))
# print(x)

# zeros = torch.zeros(2, 3)
# print(zeros)

# ones = torch.ones(2, 3)
# print(ones)

# torch.manual_seed(1729)
# random = torch.rand(2, 3)
# print(random)



# torch.manual_seed(1729)
# random1 = torch.rand(2, 3)
# print(random1)

# random2 = torch.rand(2, 3)
# print(random2)

# torch.manual_seed(1729)
# random3 = torch.rand(2, 3)
# print(random3)

# random4 = torch.rand(2, 3)
# print(random4)



x = torch.empty(2, 2, 3)
print(x.shape)
print(x)

empty_like_x = torch.empty_like(x)
print(empty_like_x.shape)
print(empty_like_x)

zeros_like_x = torch.zeros_like(x)
print(zeros_like_x.shape)
print(zeros_like_x)

ones_like_x = torch.ones_like(x)
print(ones_like_x.shape)
print(ones_like_x)

rand_like_x = torch.rand_like(x)
print(rand_like_x.shape)
print(rand_like_x)
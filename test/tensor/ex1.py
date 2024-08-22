import numpy as np

# tensor1 = np.full((2, 3, 4), 2)
# print(f"{tensor1 = }\n")

# tensor2 = np.random.randint(0, 100, size=(5, 4, 3))
# t_slice = tensor2[0, 2, :]
# print(f"{tensor2 = }\n")
# print(f"{t_slice = }\n")

tensor3_a = np.random.randint(0, 100, size=(3, 2))
tensor3_b = np.random.randint(0, 100, size=(2, 3))
print(f"{tensor3_a.shape = }")
print(f"{tensor3_b.shape = }\n")
tensor3 = np.dot((tensor3_a, tensor3_b), keepdims=True)
print(f"{tensor3 = }\n")

tensor4 = np.random.randint(0, 100, size=(2, 3, 4)).reshape((3, 8))
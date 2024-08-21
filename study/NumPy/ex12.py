import numpy as np

# a = np.arange(24).reshape((2, 3, -1))
# print(f"{a = }")

# a_sum = np.sum(a, axis=0)
# print("ndarray: {}\n{}".format(a_sum.shape, a_sum))


a = np.arange(24).reshape((2, 3, -1))
print(f"{a = }")

a_sum1 = np.sum(a, axis=2)
a_sum2 = np.sum(a, axis=2, keepdims=True)
print("ndarray: {}\n{}".format(a_sum1.shape, a_sum1))
print("ndarray: {}\n{}".format(a_sum2.shape, a_sum2))
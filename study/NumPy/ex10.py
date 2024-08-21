import numpy as np

a = np.arange(12).reshape((3, -1))
print(f"{a = }")

# print(f"{np.sum(a) = }")
# print(f"{a.sum() = }") # ndarray일때만 사용 가능

# sum_ = a.sum(axis=0)
# print("ndarray: {}\n{}".format(a.shape, a))
# print("ndarraysum(axis=0): {}\n{}".format(sum_.shape, sum_))

sum_class = np.sum(a, axis=0, keepdims=True)
sum_student = np.sum(a, axis=1, keepdims=True)
print("ndarray: {}\n{}".format(sum_class.shape, sum_class))
print("ndarray: {}\n{}".format(sum_student.shape, sum_student))
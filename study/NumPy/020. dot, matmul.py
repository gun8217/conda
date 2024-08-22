import numpy as np

u = np.random.uniform(0, 5, (4,))
v = np.random.uniform(0, 5, (4,))

sum_hadamard = np.sum(u*v)
np_dot = np.dot(u, v)

# print(f"sum_hadamard : {sum_hadamard.round(2)}")
# print(f"np_dot : {np_dot.round(2)}")

a = np.random.uniform(0, 10, (3, 4))
b = np.random.uniform(0, 10, (4, 5))

# a_shape, b_shape = a.shape, b.shape

# result = np.zeros((a_shape[0], b_shape[1]))

# for i in range(a_shape[0]):
#     for j in range(b_shape[1]):
#         for k in range(a_shape[1]):
#             result[i][j] += a[i, k] * b[k, j]
            
# print(f"{result = }")

a_shape, b_shape = a.shape, b.shape

result = np.zeros((a_shape[0], b_shape[1]))

for a_row_idx in range(a.shape[0]):
    for b_col_idx in range(b.shape[1]):
        result[a_row_idx, b_col_idx] = np.dot(a[a_row_idx, :], b[:, b_col_idx])
            
print(f"{result = }")
print()

# 행렬 내적 연산
np_matmul = np.matmul(a, b)
print(f"{np_matmul = }")
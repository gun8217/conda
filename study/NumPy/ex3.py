import numpy as np

u = [1, 2, 3]
v = [4, 5, 6]

w = u + v
print(w)

w = [u_el + v_el for u_el, v_el in zip(u, v)]
print(w)


u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
print(u + v)


M = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
N = np.array([[11, 12, 13],
              [14, 15, 16],
              [17, 18, 19]])
print(M + N)
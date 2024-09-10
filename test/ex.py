import numpy as np
import pandas as pd

u = np.array([[10, 20], [300, 400]])
v = np.array([[100, 200], [30, 40]])
e_dists = np.sqrt(np.sum((u - v)**2, axis=1))
# print(e_dists)
# print()

data_unique = [1, 1, 1, 1, 2, 5, 3, 6, 8, 9, 1, 2, 8, 9, 3, 4, 0, 9]
uniques, count = np.unique(data_unique, return_counts=True)
# print(uniques, count)
# print()

df = pd.DataFrame([1, 2, 3, 4, 5])
if 'posterior' in df.columns:
    df['prior'] = df['posterior']

x = 1; mean = 0; std = 1
y = 1 / (2*np.pi * std**2)**0.5 * np.exp(-(x - mean)**2 / (2 * std**2))

object_ = pd.DataFrame([10, 20, 30])
# print(type(object_))
# print(object_.shape)
# for attr in dir(object_):
#     if not attr.startswith('__'):print(object_)
#     break


a = np.array([1, 4, 3, 1])
print(np.sort(a))
print(np.sort(a)[::-1])
print()

b = np.array([[1, 4], [3, 1]])
print(np.sort(b.flatten())[::-1].reshape(2, -1))
print(np.sort(b, axis=None))
print(np.sort(b, axis=0))
print(np.sort(b, axis=1))
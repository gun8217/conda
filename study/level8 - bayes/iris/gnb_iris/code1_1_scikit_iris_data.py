import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
# print(type(iris))

# for attr in dir(iris):
#     if not attr.startswith('__'): print(attr)

'''DESCR
data
data_module
feature_names
filename
frame
target
target_names

'''
print("===== iris.data =====")
print(f"type: {type(iris.data)}")
print(f"shape: {iris.data.shape}")
print(f"dtype: {iris.data.dtype}")
print(f"head: \n{iris.data[:10, :]}\n")
# # print(f"head: {iris.data[:10]}") column을 전체 뽑을 땐 이렇게 간단하게 써도 됨

print("===== iris.feature_names =====")
print(f"type: {type(iris.feature_names)}")
print(f"len: {len(iris.feature_names)}")
print(f"feature names:, {iris.feature_names}\n")

print("===== iris.target =====")
print(f"type: {type(iris.target)}")
print(f"shape: {iris.target.shape}")
print(f"dtype: {iris.target.dtype}")
print(f"head: {iris.target[:10]}")
print(f"tail: {iris.target[-10:]}\n")

print("===== iris.target_names =====")
print(f"type: {type(iris.target_names)}")
print(f"shape: {iris.target_names.shape}")
print(f"dtype: {iris.target_names.dtype}")
print(f"head: {iris.target_names}")

print()

uniques, cnts = np.unique(iris.target, return_counts=True)
print(f"unique values: {uniques}")
print(f"unique counts: {cnts}\n")
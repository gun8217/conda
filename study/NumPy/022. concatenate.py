import numpy as np

# a = np.random.randint(0, 10, (3,))
# b = np.random.randint(0, 10, (4,))
# c = np.random.randint(0, 10, (5,))

# print(f"a: {a.shape}\n{a}")
# print(f"b: {b.shape}\n{b}\n")

# concat = np.concatenate([a, b, c])
# concat0 = np.concatenate([a, b, c], axis=0)

# print(f"concat: {concat.shape}\n{concat}")
# print(f"concat0: {concat0.shape}\n{concat0}")


# a = np.random.randint(0, 10, (1, 3))
# b = np.random.randint(0, 10, (1, 3))

# print(f"a: {a.shape}\n{a}")
# print(f"b: {b.shape}\n{b}\n")

# concat0 = np.concatenate([a, b], axis=0)
# concat1 = np.concatenate([a, b], axis=1)

# print(f"concat0: {concat0.shape}\n{concat0}")
# print(f"concat1: {concat1.shape}\n{concat1}")


a = np.random.randint(0, 10, (3, 4, 5))
b = np.random.randint(0, 10, (1, 4, 5))
c = np.random.randint(0, 10, (3, 1, 5))
d = np.random.randint(0, 10, (3, 4, 1))

print(f"a: {a.shape}\n{a}")
print(f"b: {b.shape}\n{b}\n")

concat0 = np.concatenate([a, b], axis=0)
concat1 = np.concatenate([a, c], axis=1)
concat2 = np.concatenate([a, d], axis=2)

print(f"concat0: {concat0.shape}\n{concat0}")
print(f"concat1: {concat1.shape}\n{concat1}")
print(f"concat2: {concat2.shape}\n{concat2}")
import numpy as np

a = np.random.randint(0, 10, (4,))
b = np.random.randint(0, 10, (4,))

# print(f"a: {a.shape}\n{a}")
# print(f"b: {b.shape}\n{b}\n")

# vstack = np.vstack([a, b])
# hstack = np.hstack([a, b])

# print(f"vstack: {vstack.shape}\n{vstack}")
# print(f"hstack: {hstack.shape}\n{hstack}")


# a2 = np.random.randint(0, 10, (1,3))
# b2 = np.random.randint(0, 10, (1,3))

# print(f"a2: {a2.shape}\n{a2}")
# print(f"b2: {b2.shape}\n{b2}\n")

# vstack2 = np.vstack([a2, b2])
# hstack2 = np.hstack([a2, b2])

# print(f"vstack: {vstack2.shape}\n{vstack2}")
# print(f"hstack: {hstack2.shape}\n{hstack2}")


# a2 = np.random.randint(0, 10, (3,1))
# b2 = np.random.randint(0, 10, (3,1))

# print(f"a2: {a2.shape}\n{a2}")
# print(f"b2: {b2.shape}\n{b2}\n")

# vstack2 = np.vstack([a2, b2])
# hstack2 = np.hstack([a2, b2])

# print(f"vstack: {vstack2.shape}\n{vstack2}")
# print(f"hstack: {hstack2.shape}\n{hstack2}")


a2 = np.random.randint(0, 10, (3,4))
b2 = np.random.randint(0, 10, (4,))

print(f"a2: {a2.shape}\n{a2}")
print(f"b2: {b2.shape}\n{b2}\n")

vstack2 = np.vstack([a2, b2])
# hstack2 = np.hstack([a2, b2])

print(f"vstack: {vstack2.shape}\n{vstack2}")
# print(f"hstack: {hstack2.shape}\n{hstack2}")
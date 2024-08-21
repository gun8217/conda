import numpy as np

a = np.random.randint(-5, 5, (5,))
b = np.random.randint(-5, 5, (5,))

print("a:", a)
print("b:", b)

print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
print("a / b:", a / b)
print("a // b:", a // b)
print("a % b:", a % b)
print("a ** b:", a.astype(float) ** b)

print("a > b:", a > b)
print("a >= b:", a >= b)
print("a < b:", a < b)
print("a <= b:", a <= b)
print("a == b:", a == b)
print("a != b:", a != b)

import numpy as np

a = np.array(3)
u = np.arange(1, 5)

shapes = "shapes: {}/{}"
print(shapes.format(a.shape,
                    u.shape))
print("a: ", a)
print("u: ", u, '\n')

print("a + u:", a + u)
print("a - u:", a - u)
print("a * u:", a * u)
print("a / u:", a / u)
print("a // u:", a // u)
print("a % u:", a % u)
print("a ** u:", a ** u)

print("a > u:", a > u)
print("a >= u:", a >= u)
print("a < u:", a < u)
print("a <= u:", a <= u)
print("a == u:", a == u)
print("a != u:", a != u)
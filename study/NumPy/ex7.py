import numpy as np

A = np.arange(24).reshape((2, 3, 4))
B = 10*np.arange(4)
C = A + B

shapes = "shapes: {}/{}/{}"
print(shapes.format(A.shape,
                    B.shape,
                    C.shape))
print(A)
print(B)
print(C)
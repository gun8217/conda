def f(x1, x2): return x1**2 + x2**2
def df_dx(x): return 2*x

x1, x2 = 3, -2
ITERATIONS = 10
LR = 0.1

print(f"Initial (x1, x2): ({x1}, {x2})")
print(f"Initial y: {f(x1, x2)}\n")

for iter in range(ITERATIONS):
    dy_dx1 = df_dx(x1)
    dy_dx2 = df_dx(x2)
    x1 = x1 - LR * dy_dx1
    x2 = x2 - LR * dy_dx2
    print(f"{iter + 1}-th (x1, x2): ({x1:.3f}, {x2:.3f})")
    print(f"y: {f(x1, x2):.3f}\n")
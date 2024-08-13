from ex1 import *

def test_function():
    x = 10
    print(f"Locals: {locals()}")
    print("function terninated\n")

test_function()
print(f"Global")
print_vars(globals())
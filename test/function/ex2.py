from ex1 import *

def test_function():
    print(locals())
    x = 10
    print(locals())

a = 10
test_function()
print()
print_vars(globals())
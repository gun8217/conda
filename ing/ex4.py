from utils import *

data = [1, 50, 100, 20, 30]
print("Descending:", func_descending(data, descending=True))
print("Ascending:", func_descending(data, descending=False))


print("Descending:", sort(data, descending=True))
print("Ascending:", sort(data, descending=False))
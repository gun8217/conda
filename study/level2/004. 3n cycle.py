# 3n cycle
num = int(input("Enter a number : "))

if num % 3 == 0:
    print(f"{num} is 3n")
elif num % 3 == 1:
    print(f"{num} is 3n + 1")
else:
    print(f"{num} is 3n + 2")
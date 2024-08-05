num = int(input("Enter a number: "))

divisor_list = [divisor 
                for divisor in range(2, num)
                if num % divisor == 0]
print(f"{divisor_list = }")

if len(divisor_list) == 0:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
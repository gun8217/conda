from Include_module import  (say_hollow_to, func1)

name1, name2, name3 = 'Yang', 'Kim', 'Park'
print(f"{say_hollow_to(name1)}\n")

data1, data2, data3 = 1, 2, 3
print(f"{func1(data2)}\n")

print(f"{func2(name3, data1)}") # 호출하지 않은 함수라 error
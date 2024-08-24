test_list = [1, 2, 3]

# shallow copy : 얕은 복사 - 새로운 memory 할당 x, bug의 위험성 있음
test_list2 = test_list
test_list2[0] = 100
print(f"{test_list = }")
print(f"{test_list2 = }\n")

# deep copy : 깊은 복사(복제) - 원본 훼손의 위험성은 없지만, 
test_list3 = test_list.copy()
test_list3[0] = 1000
print(f"{test_list = }")
print(f"{test_list3 = }")
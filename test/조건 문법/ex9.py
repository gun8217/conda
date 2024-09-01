string = input("Hello World : ")

upper_list = {}
for char in string:
    ascii_ = ord(char)
    print(f"{char}: {ascii_}")
    if 65 <= ascii_ <= 90:
        upper_list[char] = ascii_
        
print(upper_list.items())
# print("\n대문자:")
# for char, ascii_ in upper_list.items():
#     print(f"{char}: {ascii_}")
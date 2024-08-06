test_string = "aabbbbcccccd"

cnt_dict = {}
for char in test_string:
    cnt_dict[char] = cnt_dict.get(char, 0) + 1
print(cnt_dict)
print()

test_string2 = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
cnt_dict2 = {}
for char2 in test_string2:
    if char2 in cnt_dict2:
        cnt_dict2[char2] += 1
    else:
        cnt_dict2[char2] = 1
print(cnt_dict2)
print()

test_dict3 = {'a':0, 'b':1, 'c':2}
for key3 in test_dict3:
    # print(key3)
    value = test_dict3[key3]
    print(f"{key3} - {value}")
print()
for key4, value4 in test_dict3.items():
    print(f"{key4} - {value4}")
print()

# 공백을 제외하고 가장 많이 나온 문자와 나온 횟수
cnt_dict4 = {}
for char4 in test_string2:
    if char4 in cnt_dict4: cnt_dict[char] += 1
    else: cnt_dict4[char] = 1

max_char = None; max_count = 0
for char, count in cnt_dict.items():
    if char == ' ': continue # 공벡 제거
    if max_char == None or count > max_count:
        max_char = char
        max_count = count
print(f"{max_char = }, {max_count = }")
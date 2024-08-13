# test_list = [1, 2, 3]
# test_list[0] = 10
# print(test_list)

# test_dict = {'a':1, 'b':2}
# test_dict['a'] = 10
# print(test_dict)

# test_string = "hellow world"
# print(test_string[0])

# test_string[0] = 'Z'

# test_tuple = (1, 2, 3)
# print(test_tuple[0])

# test_tuple[0] = 10


def edit_list(test_list):
    print(test_list)
    test_list = test_list.copy()
    test_list[0] = 10
    print(test_list,'\n')


def edit_dict(test_dict):
    print(test_dict)
    test_dict = test_dict.copy()
    test_dict['a'] = 10
    print(test_dict)


test_list = [1, 2, 3]
edit_list(test_list)

test_dict = {'a':1, 'b':2}
edit_dict(test_dict)
# a = 1, 2, 3
# print(a)

# a, b, c = [1, 2, 3]
# print(a, b, c)


# test_list = [1, 2, 3, 4, 5]
# a, b, *c = test_list
# print(a, b, c, sep='   ')


def test_function(param1, param2, param3):
    print(f"{param1 = }, {param2 = }, {param3 = }")


test_function(*[1, 2, 3])
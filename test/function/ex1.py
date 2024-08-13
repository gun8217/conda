def print_vars(namespace_dict):
    namespace_dict = namespace_dict.copy()
    for name, obj in namespace_dict.items():
        if not name.startswith('__'):
            print(f"{name}:{obj}")
    print()


if __name__ == '__main__':
    test_int = 1
    test_list = [1, 2, 3]
    print_vars(globals())


def print_params(a, *args, b=10, **kwargs):
    print(f"{a = }")
    print(f"{args = }")
    print(f"{b = }")
    print(f"{kwargs = }\n")


if __name__ == '__main__':
    # print_params()
    print_params(1)
    print_params(1, 10, 20, 100, 1000)
    print_params(1, 10, 20, b=100, kw1=100, kw2=200)
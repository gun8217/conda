def say_hollow_to(name):
    save_name = 'hellow ' + name + '!'
    return save_name


def func1(data):
    save_data = data
    return save_data


def func2(name, data):
    return f"togerder = {say_hollow_to(name)}, {func1(data)}"
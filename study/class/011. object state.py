# object의 state 예시 : name, age는 method가 아니라 state


class Human:
    pass


human1, human2 = Human(), Human()

human1.name, human1.age = "Shin", 30
human2.name, human2.age = "Yang", 25

print(human1.name, human1.age)
print(human2.name, human2.age)
# __init__ : 객체 생성과 동시에 실행

class Person:
    def __init__(self, name):
        self.name = name

        self.say_hollo()

    def say_hollo(self):
        print("Hello! I'm", self.name)

person1, person2 = Person('Yang'), Person('Shin')
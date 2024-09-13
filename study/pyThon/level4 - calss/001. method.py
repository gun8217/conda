# method 생성(def)과 호출(.메서드명())

class Person:
    def say_hello(self):
        print('Hellow!')

    def say_bye(self):
        print('Goodbye!')


Person1, Person2 = Person(), Person()
print(Person1.say_hello())
print(Person1.say_bye())
print()
print(Person2.say_hello())
print(Person2.say_bye())
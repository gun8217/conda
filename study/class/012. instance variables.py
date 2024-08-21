

class Human:
    def init_human(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_name_age(self):
        return self.name, self.age


human = Human()
human.init_human('Yang', 30)
print(human.get_name(), human.get_age())
print(human.get_name_age())
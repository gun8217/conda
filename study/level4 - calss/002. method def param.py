# method def param

class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def get_family_name(self):
        return self.name[0]
    
    def get_personal_name(self):
        return self.name[1:]


Person1 = Person()
Person1.set_name('김철수')

print(Person1.get_name())
print(Person1.get_family_name())
print(Person1.get_personal_name())
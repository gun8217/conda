from utils import print_attributes


class Character:
    def __init__(self, HP, ATK):
        self.lv = 1
        self.HP = HP
        self.ATK = ATK
    
    def get_lv(self): return self.lv
    def get_HP(self): return self.HP
    def get_ATK(self): return self.ATK


class Knigth(Character):
    def __init__(self, name, HP, ATK):
        super().__init__(HP, ATK)
        self.name = name

    def get_name(self): return self.name


knigth = Knigth('Shin', 100, 10)
print_attributes(knigth)
print(knigth.get_name())
print(knigth.get_lv())
print(knigth.get_HP())
print(knigth.get_ATK())
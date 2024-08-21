from utils import print_attributes


class UserCharacter:
    def attack(self):
        print("일반 공격!")


class Knigth(UserCharacter):
    def repeating_slach(self):
        print("[기사] 연속 베기!")


user_char = UserCharacter()
print_attributes(user_char)

knigth = Knigth()
print_attributes(knigth)
knigth.repeating_slach()
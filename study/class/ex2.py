from utils import print_attributes


class UserCharacter:
    def attack(self):
        print("일반 공격!")


class Knigth(UserCharacter):
    def attack(self):
        print("[기사] 일반 공격!")

    def repeating_slach(self):
        print("[기사] 연속 베기!")


class Magician(UserCharacter):
    def attack(self):
        super().attack()
        print("[마법사] 일반 공격!")

    def fire_ball(self):
        print("[마법사] 화염 공 던지기!")


class Archer(UserCharacter):
    def double_shot(self):
        print("[궁사] 화살 두개 쏘기!")


knigth, magician, archer = Knigth(), Magician(), Archer()
print_attributes(knigth)
print_attributes(magician)
print_attributes(archer)

knigth.attack()
knigth.repeating_slach()
magician.attack()
magician.fire_ball()
archer.double_shot()
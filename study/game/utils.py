class Character:
    def __init__(self, name, health, attack, defense):
        # 생성자: 캐릭터의 기본 정보를 초기화합니다.
        self.name = name  # 캐릭터의 이름
        self.health = health  # 캐릭터의 체력
        self.attack = attack  # 캐릭터의 공격력
        self.defense = defense  # 캐릭터의 방어력
        self.experience = 0  # 캐릭터의 현재 경험치
        self.level = 1  # 캐릭터의 현재 레벨
        self.experience_to_level_up = 100  # 레벨업에 필요한 경험치 양

    def take_damage(self, damage):
        # 피해를 받고 체력을 감소시키는 메서드
        damage_taken = max(damage - self.defense, 0)  # 방어력을 고려한 실제 피해량 계산
        self.health -= damage_taken  # 체력 감소
        if self.health < 0:
            self.health = 0  # 체력이 0보다 낮아지면 0으로 설정
        print(f"{self.name}이(가) {damage_taken}의 피해를 입었습니다. 현재 체력: {self.health}")

    def attack_opponent(self, opponent):
        # 상대 캐릭터를 공격하는 메서드
        print(f"{self.name}이(가) {opponent.name}을(를) 공격합니다!")
        opponent.take_damage(self.attack)  # 공격력에 따라 상대 캐릭터에게 피해를 줍니다.
        if not opponent.is_alive():  # 상대 캐릭터가 죽었는지 확인
            self.gain_experience(50)  # 적을 처치했을 때 경험치를 획득합니다.

    def gain_experience(self, amount):
        # 경험치를 얻는 메서드
        self.experience += amount  # 경험치 증가
        print(f"{self.name}이(가) {amount}의 경험치를 얻었습니다. 현재 경험치: {self.experience}/{self.experience_to_level_up}")
        while self.experience >= self.experience_to_level_up:  # 레벨업 조건 확인
            self.level_up()  # 레벨업 처리

    def level_up(self):
        # 레벨업을 처리하는 메서드
        self.experience -= self.experience_to_level_up  # 레벨업 후 남은 경험치 설정
        self.level += 1  # 레벨 증가
        self.experience_to_level_up = int(self.experience_to_level_up * 1.5)  # 다음 레벨업에 필요한 경험치 증가
        self.health += 10  # 레벨업 시 체력 증가
        self.attack += 5   # 레벨업 시 공격력 증가
        self.defense += 2  # 레벨업 시 방어력 증가
        print(f"{self.name}이(가) 레벨업했습니다! 현재 레벨: {self.level}, 체력: {self.health}, 공격력: {self.attack}, 방어력: {self.defense}")

    def is_alive(self):
        # 캐릭터가 살아있는지 확인하는 메서드
        return self.health > 0

    def __str__(self):
        # 캐릭터의 정보를 문자열로 반환하는 메서드
        return (f"이름: {self.name}\n"
                f"레벨: {self.level}\n"
                f"체력: {self.health}\n"
                f"공격력: {self.attack}\n"
                f"방어력: {self.defense}\n"
                f"경험치: {self.experience}/{self.experience_to_level_up}")

# 사용 예시
if __name__ == "__main__":
    hero = Character("용사", 100, 20, 10)  # 주인공 캐릭터 생성
    monster = Character("몬스터", 80, 15, 5)  # 적 캐릭터 생성

    print(hero)  # 주인공 캐릭터의 정보 출력
    print(monster)  # 적 캐릭터의 정보 출력

    hero.attack_opponent(monster)  # 주인공이 적을 공격
    if monster.is_alive():  # 적이 살아있다면 반격
        monster.attack_opponent(hero)

    print(hero)  # 주인공 캐릭터의 정보 출력
    print(monster)  # 적 캐릭터의 정보 출력
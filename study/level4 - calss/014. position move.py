import os


class Human:
    def _print_location(self):
        print("Current location:", f"{self.x_location}, {self.y_location}")

    def init_location(self):
        self.x_location = 0
        self.y_location = 0
        self._print_location()

    def move_left(self):
        self.x_location += 1
        self._print_location()

    def move_right(self):
        self.x_location -= 1
        self._print_location()

    def move_up(self):
        self.y_location += 1
        self._print_location()

    def move_down(self):
        self.y_location -= 1
        self._print_location()


human = Human()
human.init_location()

while True:
    move = input("[1] 위로 이동 [2] 아래로 이동 \n [3] 오른쪽으로 이동 [4] 왼쪽으로 이동:")
    os.system('cls') # clear
    if move == '1' : human.move_up()
    elif move == '2' : human.move_down()
    elif move == '3' : human.move_right()
    elif move == '4' : human.move_left()
    else: raise ValueError("[Error] Invalid Input")
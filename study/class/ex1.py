import os


class Human:
    def _print_location(self):
        print("Current location:", f"{self.x_location}, {self.y_location}")

    def init_location(self):
        self.x_location = 0
        self.y_location = 0
        self._print_location()

    def move_forward(self):
        self.x_location += 1
        self._print_location()

    def move_backward(self):
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
human.move_forward()
human.move_forward()
human.move_forward()
human.move_backward()
human.move_backward()
human.move_up()
human.move_up()
human.move_up()
human.move_down()
human.move_down()


class Human:
    def _print_current_location(self):
        print("Current location:", self.location)

    def init_location(self):
        self.location = 0
        self._print_current_location()
        # return self.location()

    def move_forward(self):
        self.location += 1
        self._print_current_location()

    def move_backward(self):
        self.location -= 1
        self._print_current_location()


human = Human()
human.init_location()
human.move_forward()
human.move_forward()
human.move_forward()
human.move_backward()
human.move_backward()
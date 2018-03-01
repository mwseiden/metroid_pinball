

from .strip import Strip

class DynamicBackBoxShow:

    BASE_LEFT = 128
    BASE_RIGHT = 192
    STRIP_LENGTH = 10

    def __init__(self, machine):
        self.machine = machine
        self.frame = 0

        self.left_z_front = Strip(machine, self.BASE_LEFT, self.STRIP_LENGTH, True)
        self.left_z_middle = Strip(machine, self.BASE_LEFT + self.STRIP_LENGTH, self.STRIP_LENGTH, False)
        self.left_z_rear = Strip(machine, self.BASE_LEFT + (self.STRIP_LENGTH * 2), self.STRIP_LENGTH, True)
        self.left_x_left = self.left_z_middle
        self.left_x_middle = Strip(machine, self.BASE_LEFT + (self.STRIP_LENGTH * 3), self.STRIP_LENGTH, False)
        self.left_x_right = Strip(machine, self.BASE_LEFT + (self.STRIP_LENGTH * 4), self.STRIP_LENGTH, True)

        self.right_z_front = Strip(machine, self.BASE_RIGHT, self.STRIP_LENGTH, True)
        self.right_z_middle = Strip(machine, self.BASE_RIGHT + self.STRIP_LENGTH, self.STRIP_LENGTH, False)
        self.right_z_rear = Strip(machine, self.BASE_RIGHT + (self.STRIP_LENGTH * 2), self.STRIP_LENGTH, True)
        self.right_x_right = self.right_z_middle
        self.right_x_middle = Strip(machine, self.BASE_RIGHT + (self.STRIP_LENGTH * 3), self.STRIP_LENGTH, False)
        self.right_x_left = Strip(machine, self.BASE_RIGHT + (self.STRIP_LENGTH * 4), self.STRIP_LENGTH, True)

        self.strips = [
            self.left_z_front,
            self.left_z_middle,
            self.left_z_rear,
            self.left_x_middle,
            self.left_x_right,
            self.right_z_front,
            self.right_z_middle,
            self.right_z_rear,
            self.right_x_middle,
            self.right_x_left]

        self.strip_count = len(self.strips)

    def animate(self):
        self.frame += 1

    def is_finished(self):
        return False

    def save_state(self):
        for strip in self.strips:
            strip.save_state()

    def restore_state(self):
        for strip in self.strips:
            strip.restore_state()

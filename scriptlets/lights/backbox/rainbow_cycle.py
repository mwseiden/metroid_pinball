from .dynamic_backbox_show import DynamicBackBoxShow
from .wheel import Wheel

class RainbowCycle(DynamicBackBoxShow):

    def __init__(self, machine, increment):
        super().__init__(machine)

        self.j = 0
        self.increment = increment
        self.wheel = Wheel()


    def animate(self):
        super().animate()

        for strip_number in range(0, 10):
            for i in range(0, self.strips[strip_number].size):
                self.strips[strip_number].set_color(i, self.wheel.at(self.j + i))

        self.j += self.increment
        if self.j > 255:
            self.j %= 255

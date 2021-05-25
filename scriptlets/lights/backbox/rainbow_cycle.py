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

        for strip in self.strips:
            for i in range(0, strip.size):
                strip.set_color(i, self.wheel.at(((i * 256 / strip.size) + self.j) % 256))

        self.j += self.increment
        if self.j > 255:
            self.j %= 256

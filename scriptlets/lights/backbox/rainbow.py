from random import randint

from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Rainbow(DynamicBackBoxShow):
    COLORS = [
        RGBColor([40, 0, 0]),
        RGBColor([40, 40, 0]),
        RGBColor([0, 40, 0]),
        RGBColor([0, 40, 40]),
        RGBColor([0, 0, 40]),
        RGBColor([40, 0, 40])
    ]

    def __init__(self, machine, speed):
        super().__init__(machine)

        self.speed = speed
        self.column_positions = [0] * self.strip_count

        for strip_number in range(self.strip_count):
            self.column_positions[strip_number] = randint(0, self.strips[strip_number].size)

    def animate(self):
        super().animate()

        if self.frame % self.speed == 0:
            for strip_number in range(self.strip_count):
                self.column_positions[strip_number] += 1
                for light_number in range(12):
                    index = (light_number + self.column_positions[strip_number]) % 12
                    if strip_number % 2 == 0:
                        index = 11 - index
                    self.strips[strip_number].set_color(index, self.COLORS[light_number % len(self.COLORS)])

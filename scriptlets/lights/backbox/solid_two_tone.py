from random import randint

from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class SolidTwoTone(DynamicBackBoxShow):
    def __init__(self, machine, min_cutoff, max_cutoff, color1, color2):
        super().__init__(machine)

        self.cutoff = [0] * self.strip_count
        self.min_cutoff = min_cutoff
        self.max_cutoff = max_cutoff
        self.color1 = color1
        self.color2 = color2

        for strip_number in range(self.strip_count):
            self.cutoff[strip_number] = randint(min_cutoff, max_cutoff)

    def animate(self):
        if self.frame != 0:
            return

        super().animate()

        for strip_number in range(self.strip_count):
            for light_number in range(0, self.strips[strip_number].size):
                self.strips[strip_number].set_color(
                    light_number,
                    self.color1 if light_number < self.cutoff[strip_number] else self.color2
                )

from random import randint

from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class CloudyLandscape(DynamicBackBoxShow):
    GROUND_COLOR = RGBColor([4, 16, 12])
    SKY_COLOR = RGBColor([4, 4, 4])

    def __init__(self, machine):
        super().__init__(machine)

        self.cutoff = [0] * self.strip_count

        for strip_number in range(self.strip_count):
            self.cutoff[strip_number] = 10 - randint(2, 4)

    def animate(self):
        if self.frame != 0:
            return

        super().animate()

        for strip_number in range(self.strip_count):
            for light_number in range(0, self.strips[strip_number].size):
                self.strips[strip_number].set_color(
                    light_number,
                    self.GROUND_COLOR if light_number >= self.cutoff[strip_number] else self.SKY_COLOR
                )

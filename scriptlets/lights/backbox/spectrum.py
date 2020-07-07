# from random import randint

from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Spectrum(DynamicBackBoxShow):

    def __init__(self, machine, color1, color2, color3):
        super().__init__(machine)

        self.colors = self.blend(color1, color2) + self.blend(color3, color3) + self.blend(color3, color1)

        self.position = 0

    def animate(self):
        super().animate()

        for strip in self.strips:
            for index in range(10):
                strip.set_color(index, self.colors[(self.position + index + 30) % 30])

        self.position += 1

        if self.position == 30:
           self.position = 0

    def blend(self, c1, c2):
        colors = []

        for index in range(10):
            colors.append(RGBColor.blend(c1, c2, 0.1 * index))

        return colors

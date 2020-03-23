from random import randint

from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Gradient(DynamicBackBoxShow):
    def __init__(self, machine, color_start, color_end):
        super().__init__(machine)

        self.color_start = color_start
        self.color_end = color_end

        self.colors = []

        r1, g1, b1 = self.color_start.rgb
        r2, g2, b2 = self.color_end.rgb

        for index in range(10):
            r = r1 + (r2 - r1) * index / 9
            g = g1 + (g2 - g1) * index / 9
            b = b1 + (b2 - b1) * index / 9

            self.colors.append(RGBColor([r,g,b]))

    def animate(self):
        super().animate()

        for strip in self.strips:
            for index in range(10):
                strip.set_color(index, self.colors[index])

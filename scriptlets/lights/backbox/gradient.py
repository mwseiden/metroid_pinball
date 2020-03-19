from random import randint

from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Gradient(DynamicBackBoxShow):
    def __init__(self, machine, color_start, color_end):
       super().__init__(machine)

       self.color_start = color_start
       self.color_end = color_end

    def animate(self):
        super().animate()

        r1, g1, b1 = self.color_start.rgb
        r2, g2, b2 = self.color_end.rgb

        for strip in self.strips:
            for index in range(10):
                r = ((r1 - r2) * 10) / (index + 1)
                g = ((g1 - g2) * 10) / (index + 1)
                b = ((b1 - b2) * 10) / (index + 1)

                strip.set_color(index, RGBColor([abs(r), abs(g), abs(b)]))

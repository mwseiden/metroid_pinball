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


        for strip in self.strips:
            for index in range(10):
                r = ((self.color_start.r - self.color_end.r) * (index + 1)) / 10
                g = ((self.color_start.g - self.color_end.g) * (index + 1)) / 10
                b = ((self.color_start.b - self.color_end.b) * (index + 1)) / 10

                strip.set_color(index, RGBColor([r,g,b]))

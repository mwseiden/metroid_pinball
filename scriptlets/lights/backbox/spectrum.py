# from random import randint

from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Spectrum(DynamicBackBoxShow):

    def __init__(self, machine, color1, color2, color3):
        super().__init__(machine)

        self.colors = [color1, color2, color3, color1, color2]

        self.primary_color = 0
        self.position = 0

        # for strip_number in range(self.strip_count):
        #     self.column_positions[strip_number] = randint(0, self.strips[strip_number].size)

    def animate(self):
        super().animate()

        for strip in self.strips:
            for index in range(10):
                strip.set_color(index, RGBColor.blend(self.colors[self.primary_color], self.colors[self.primary_color + 1], (index + self.position) * 0.1))
                strip.set_color(index, RGBColor.blend(self.colors[self.primary_color + 1], self.colors[self.primary_color + 2], ((index + self.position + 10) % 10) * 0.1))

        self.position += 1

        if self.position == 10:
           self.position = 0
           self.primary_color += 1

           if self.primary_color > 2:
             self.primary_color = 0

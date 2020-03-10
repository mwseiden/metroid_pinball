from random import randint

from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class HeatUp(DynamicBackBoxShow):
    def __init__(self, machine, color, add_percentage, steps):
        super().__init__(machine)

        self.color = color
        self.add_percentage = add_percentage
        self.steps = steps
        self.current_step = 0

    def animate(self):
        super().animate()

        if self.frame % 5 == 0:
            for strip_number in range(self.strip_count):
                for index in range(10):
                    value = (self.add_percentage * 10) - ((index + 1) * self.add_percentage) + (self.current_step * self.add_percentage)
     
                    if value > 100:
                        value = 100

                    r, g, b = self.color.rgb
                    r = r * value / 100
                    g = g * value / 100
                    b = b * value / 100

                    self.strips[strip_number].set_color(index, RGBColor([r,g,b]))
       
                    self.current_step = self.current_step + 1 


    def is_finished(self):
        return self.current_step >= self.steps

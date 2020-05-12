from random import randint

from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Twinkle(DynamicBackBoxShow):
    def __init__(self, machine, background_color, twinkle_color, twinkle_count, steps):
       super().__init__(machine)

       self.background_color = background_color
       self.twinkle_color = twinkle_color
       self.twinkle_count = twinkle_count
       self.steps = steps

       self.generate_twinkles()

    def animate(self):
        super().animate()

        for twinkle in self.twinkles:
            r1, g1, b1 = self.twinkle_color.rgb
            r2, g2, b2 = self.background_color.rgb

            color = RGBColor([
                r1 + (r2 - r1) * (twinkle[2] % (self.steps + 1)) / self.steps,
                g1 + (g2 - g1) * (twinkle[2] % (self.steps + 1)) / self.steps,
                b1 + (b2 - b1) * (twinkle[2] % (self.steps + 1)) / self.steps
            ])

            if twinkle[3] == 0:
                twinkle[2] = twinkle[2] + 1
                if twinkle[2] > self.steps:
                    twinkle[2] = self.steps
                    twinkle[3] = 1
            else:
                twinkle[2] = twinkle[2] - 1
                if twinkle[2] < 1:
                    twinkle[0] = randint(0, self.strip_count - 1)
                    twinkle[1] = randint(0, 9)
                    twinkle[2] = 1
                    twinkle[3] = 0

            self.strips[twinkle[0]].set_color(twinkle[1], color)

    def generate_twinkles(self):
        self.twinkles = [[0, 0, 0, 0]] * self.twinkle_count

        for strip_number in range(self.strip_count):
            self.strips[strip_number].set_all_colors(self.background_color)

        for twinkle_number in range(self.twinkle_count):
            self.twinkles[twinkle_number] = [randint(0, self.strip_count - 1), randint(0, 9), randint(1, 100), randint(0, 1)]

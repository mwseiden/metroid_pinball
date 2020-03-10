from random import randint

from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Sparkle(DynamicBackBoxShow):
    def __init__(self, machine, background_color, sparkle_color, sparkle_count, repeat):
        super().__init__(machine)

        self.background_color = background_color
        self.sparkle_color = sparkle_color
        self.sparkle_count = sparkle_count
        self.repeat = repeat
        self.done = False
        self.sparkle_indexes = [0] * self.sparkle_count
        self.sparkle_strips = [0] * self.sparkle_count

        self.generate_sparkles()

    def animate(self):
        super().animate()

        for sparkle_number in range(self.sparkle_count):
            self.strips[self.sparkle_strips[sparkle_number]].set_color(self.sparkle_indexes[sparkle_number], self.sparkle_color)

        if not self.done:
            for strip_number in range(self.strip_count):
                self.strips[strip_number].set_all_colors(self.background_color)

            if self.repeat > 0:
                self.repeat = self.repeat - 1

            if self.repeat == 0:
                self.done = True

            self.generate_sparkles()

    def generate_sparkles(self):
        for sparkle_number in range(self.sparkle_count):
            self.sparkle_indexes[sparkle_number] = randint(0, 9)
            self.sparkle_strips[sparkle_number] = randint(0, 9)

    def is_finished(self):
        return self.done

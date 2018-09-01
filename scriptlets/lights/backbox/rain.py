from random import randint

from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Rain(DynamicBackBoxShow):

    SKY_COLOR = RGBColor([0, 0, 4])
    DROP_COLOR = RGBColor([16, 16, 32])

    START_POSITION = -2

    MINIMUM_DELAY = 1
    MAXIMUM_DELAY = 2

    def __init__(self, machine):
        super().__init__(machine)

        # each drop has velocity and position
        self.velocities = [0] * self.strip_count
        self.positions = [0] * self.strip_count

        # one drop per strip
        for strip_number in range(self.strip_count):
            self._new_drop(strip_number)
            self.strips[strip_number].set_all_colors(self.SKY_COLOR)

    def animate(self):
        super().animate()

        for strip_number in range(self.strip_count):
            if self.frame % self.velocities[strip_number] == 0:
                self.strips[strip_number].set_color(self.positions[strip_number], self.SKY_COLOR)
                self.strips[strip_number].set_color(self.positions[strip_number] + 1, self.DROP_COLOR)
                self.positions[strip_number] += 1

                if self.positions[strip_number] >= len(self.strips):
                    self._new_drop(strip_number)

    # private ----------------------------------------------------------------

    def _new_drop(self, strip_number):
        self.velocities[strip_number] = self.MINIMUM_DELAY + randint(0, self.MAXIMUM_DELAY - self.MINIMUM_DELAY + 1)
        self.positions[strip_number] = self.START_POSITION

from random import randint

from mpf.core.rgb_color import RGBColor
from dynamic_backbox_show import DynamicBackBoxShow

class Rain(DynamicBackBoxShow):

    SKY_COLOR = RGBColor([0, 0, 8])
    DROP_COLOR = RGBColor([8, 8, 32])

    START_POSITION = -4

    MINIMUM_DELAY = 4
    MAXIMUM_DELAY = 8

    def __init__(self, machine):
        super().__init__(machine)

        # each drop has velocity and position
        self.velocities = [0] * self.strip_count
        self.positions = [0] * self.strip_count

        # one drop per strip
        for strip_number in range(0, self.strip_count):
            _new_drop(strip_number)
            self.strips[strip_number].set_all_colors(SKY_COLOR)

    def animate(self):
        super().animate()

        for strip_number in range(0, self.strip_count):
            if self.frame % self.velocities[strip_number] == 0:
                strip.set_color(self.positions[strip_number], SKY_COLOR)
                strip.set_color(self.positions[strip_number] + 1, DROP_COLOR)
                self.positions[strip_number] += 1

                if self.positions[strip_number] >= len(self.strips) _new_drop(strip_number)

    # private ----------------------------------------------------------------

    def _new_drop(strip_number):
        self.velocities[strip_number] = MINIMUM_DELAY + randint(0, MAXIMUM_DELAY - MINIMUM_DELAY + 1)
        self.positions[strip_number] = START_POSITION

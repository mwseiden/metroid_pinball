from random import randint

from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Drop(DynamicBackBoxShow):

    START_POSITION = -2

    def __init__(self, machine, min_delay, max_delay, background_color, drop_color):
        super().__init__(machine)

        self.min_delay = min_delay
        self.max_delay = max_delay
        self.background_color = background_color
        self.drop_color = drop_color

        # each drop has velocity and position
        self.velocities = [0] * self.strip_count
        self.positions = [0] * self.strip_count

        # one drop per strip
        for strip_number in range(self.strip_count):
            self._new_drop(strip_number)
            self.strips[strip_number].set_all_colors(self.background_color)

    def animate(self):
        super().animate()

        for strip_number in range(self.strip_count):
            if self.frame % self.velocities[strip_number] == 0:
                self.strips[strip_number].set_color(self.positions[strip_number], self.background_color)
                self.strips[strip_number].set_color(self.positions[strip_number] + 1, self.drop_color)
                self.positions[strip_number] += 1

                if self.positions[strip_number] >= len(self.strips):
                    self._new_drop(strip_number)

    # private ----------------------------------------------------------------

    def _new_drop(self, strip_number):
        self.velocities[strip_number] = self.min_delay + randint(0, self.max_delay - self.min_delay)
        self.positions[strip_number] = self.START_POSITION

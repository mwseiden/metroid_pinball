from random import randint
from random import choice

from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Pour(DynamicBackBoxShow):

    def __init__(self, machine, pour_count, min_length, max_length, invert, color):
        super().__init__(machine)

        self.pour_count = pour_count
        self.min_length = min_length
        self.max_length = max_length
        self.invert = invert
        self.color = color

        self.pours = [None] * self.pour_count
        self.pour_columns = [None] * self.pour_count

        for pour_number in range(self.pour_count):
            self._generate_pour(pour_number)

    def animate(self):
        if self.frame == 0:
            for strip in self.strips:
                strip.set_all_colors(self.OFF_COLOR)

        super().animate()

        for pour_number in range(self.pour_count):
            self.pours[pour_number].animate(self.invert)
            if self.pours[pour_number].is_finished():
                self._generate_pour(pour_number)

    def _generate_pour(self, index):
        self.pour_columns[index] = choice(list(set(range(self.strip_count)).difference(self.pour_columns)))
        self.pours[index] = ColumnPour(
            self.strips[self.pour_columns[index]],
            randint(self.min_length, self.max_length + 1),
            self.color
        )

class ColumnPour():
    def __init__(self, strip, length, color):
        self.strip = strip
        self.length = length
        self.color = color
        self.drops = []
        self.dripping = False
        self.current_length = 0
        self.drop_frequency = 8
        self.frame = 0

    def animate(self, invert):
        self.frame += 1

        for light_number in range(0, self.current_length):
            if invert:
                self.strip.set_color(9 - light_number, self._randomized_color())
            else:
                self.strip.set_color(light_number, self._randomized_color())

        if self.dripping:
            if self.current_length > 0 and self.frame % self.drop_frequency == 0:
                self.current_length -= 1
                self.drops += [Drop(self.strip, self.current_length, self._randomized_color())]
                if self.drop_frequency > 2:
                    self.drop_frequency -= 1

            finished_drops = []

            for drop in self.drops:
                drop.animate()
                if drop.is_finished():
                    finished_drops += [drop]

            self.drops = list(set(self.drops).difference(finished_drops))
        else:
            self.current_length += 1
            self.dripping = self.current_length >= self.length

    def is_finished(self):
        return self.dripping and self.current_length == 0 and len(self.drops) == 0

    def _randomized_color(self):
        r, g, b = self.color.rgb
        variance = 1.1 - (0.05 * randint(0, 5))

        return RGBColor([int(r * variance), int(g * variance), int(b * variance)])

class Drop():
    OFF_COLOR = RGBColor('off')

    def __init__(self, strip, position, color):
        self.strip = strip
        self.position = position
        self.color = color

    def animate(self):
        self.strip.set_color(self.position, self.OFF_COLOR)
        self.position += 1
        self.strip.set_color(self.position, self.color)

    def is_finished(self):
        return self.position >= self.strip.size


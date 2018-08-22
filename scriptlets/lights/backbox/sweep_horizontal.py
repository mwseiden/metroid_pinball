from random import randint

from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class SweepHorizontal(DynamicBackBoxShow):
    OFF_COLOR = RGBColor([0, 0, 0])

    def __init__(self, machine, color, speed, repeat, direction):
        super().__init__(machine)

        self.color = color
        self.repeat = repeat
        self.speed = speed
        self.done = False
        self.direction = direction
        self.current_sweep = 0 if direction == 0 else 5

    def animate(self):
        super().animate()

        if self.frame % self.speed == 0:
            self.strips[0].set_all_colors(self.color if self.current_sweep == 0 else self.OFF_COLOR)
            self.strips[1].set_all_colors(self.color if self.current_sweep == 0 else self.OFF_COLOR)
            self.strips[2].set_all_colors(self.color if self.current_sweep == 0 else self.OFF_COLOR)
            self.strips[3].set_all_colors(self.color if self.current_sweep == 1 else self.OFF_COLOR)
            self.strips[4].set_all_colors(self.color if self.current_sweep == 2 else self.OFF_COLOR)
            self.strips[5].set_all_colors(self.color if self.current_sweep == 3 else self.OFF_COLOR)
            self.strips[6].set_all_colors(self.color if self.current_sweep == 4 else self.OFF_COLOR)
            self.strips[7].set_all_colors(self.color if self.current_sweep == 5 else self.OFF_COLOR)
            self.strips[8].set_all_colors(self.color if self.current_sweep == 5 else self.OFF_COLOR)
            self.strips[9].set_all_colors(self.color if self.current_sweep == 5 else self.OFF_COLOR)

            self.current_sweep += 1 if direction == 0 else -1

            if self.current_sweep < 0:
                self.current_sweep = 5
                self.repeat -= 1
            elif self.current_sweep > 5
                self.current_sweep = 0
                self.repeat -= 1

            self.done = self.repeat < 0:

    def is_finished(self):
        return self.done

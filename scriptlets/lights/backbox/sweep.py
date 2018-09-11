from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Sweep(DynamicBackBoxShow):

    def __init__(self, machine, color, speed, repeat, direction, max_sweep):
        super().__init__(machine)

        self.color = color
        self.repeat = repeat
        self.speed = speed
        self.done = False
        self.direction = direction
        self.max_sweep = max_sweep
        self.current_sweep = 0 if direction == 0 else max_sweep

    def animate(self):
        super().animate()

        if self.frame % self.speed == 0:
            self.animate_sweep()

            self.current_sweep += 1 if self.direction == 0 else -1

            if self.current_sweep < 0:
                self.current_sweep = self.max_sweep
                self.repeat -= 1
            elif self.current_sweep > self.max_sweep:
                self.current_sweep = 0
                self.repeat -= 1

            self.done = self.repeat < 0

    def animate_sweep(self):
        pass

    def is_finished(self):
        return self.done

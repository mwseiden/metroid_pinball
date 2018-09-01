from mpf.core.rgb_color import RGBColor
from .sweep import Sweep

class SweepVertical(Sweep):
    def __init__(self, machine, color, speed, repeat, direction):
        super().__init__(machine, color, speed, repeat, direction, 9)

    def animate_sweep(self):
        for strip in self.strips:
            strip.set_all_colors(self.OFF_COLOR)
            strip.set_color(self.current_sweep, self.color)

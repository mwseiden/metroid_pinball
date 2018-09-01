from mpf.core.rgb_color import RGBColor
from .sweep import Sweep

class SweepHorizontal(Sweep):
    def __init__(self, machine, color, speed, repeat, direction):
        super().__init__(machine, color, speed, repeat, direction, 5)

    def animate_sweep(self):
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

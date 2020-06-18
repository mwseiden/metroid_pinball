from random import randint
from random import choice
from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Plasma(DynamicBackBoxShow):
    def __init__(self, machine, colors, decay_r, decay_g, decay_b, repeat):
        super().__init__(machine)
        self.colors = colors

        self.decay_r = decay_r
        self.decay_g = decay_g
        self.decay_b = decay_b

        if repeat == -1:
            self.repeat = None
        else:
            self.repeat = repeat

    def animate(self):
        super().animate()

        if self.repeat != None and self.frame % 30 == 0:
            self.repeat = self.repeat - 1

        for strip in self.strips:
            strip.set_color(strip.size - 1, choice(self.colors))

            for light_index in reversed(range(1, strip.size)):
                strip.set_color(light_index - 1, self._decay_colors(strip.get_color(light_index), strip.get_color(light_index - 1)))

            strip.set_color(0, self._decay_colors(strip.get_color(0), self.OFF_COLOR))

    def is_finished(self):
        return self.repeat != None and self.repeat < 0

    def _decay_colors(self, a, b):
        r1, g1, b1 = a.rgb
        r2, g2, b2 = b.rgb

        decay = 1.0 - (0.1 * randint(1, 5))
        return RGBColor([
            int(((r1 + r2) / self.decay_r) * decay),
            int(((g1 + g2) / self.decay_g) * decay),
            int(((b1 + b2) / self.decay_b) * decay)
        ])

from random import randint
from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Fire(DynamicBackBoxShow):
    OFF_COLOR = RGBColor([0, 0, 0])

    def __init__(self, machine):
        super().__init__(machine)

    def animate(self):
        super().animate()

        if self.frame > 1:
            return

        for strip in self.strips:
            highlight = randint(0, 30)
            introduced_color = RGBColor([intensity, highlight, highlight / 2])
            self.info_log('WTF: Introduced color for frame %s, index 0: %s', self.frame, introduced_color)
            strip.set_color(0, introduced_color)
            for light_index in range(1, strip.size - 1):
                averaged_color = self._average_colors(strip.get_color(light_index), strip.get_color(light_index + 1))
                self.info_log('WTF: Averaged colors for frame %s, index %s: %s', self.frame, light_index, averaged_color)
                strip.set_color(light_index + 1, averaged_color)
            intensity = randint(0, 120)
            last_color = self._average_colors(strip.get_color(strip.size - 1), self.OFF_COLOR)
            self.info_log('WTF: Last color for frame %s, index %s: %s', self.frame, strip.size - 1, last_color)
            strip.set_color(strip.size - 1, last_color)

    def _average_colors(self, a, b):
        r1, g1, b1 = a.rgb
        r2, g2, b2 = b.rgb

        return RGBColor([(r1 + r2) / 2, (g1 + g2) / 2, (b1 + b2) / 2])

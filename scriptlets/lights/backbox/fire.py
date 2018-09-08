from random import randint
from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Fire(DynamicBackBoxShow):
    FIRE_COLOR = RGBColor([80, 35, 0])
    OFF_COLOR = RGBColor([0, 0, 0])

    def __init__(self, machine):
        super().__init__(machine)

    def animate(self):
        super().animate()
        for strip in self.strips:
            for light_index in range(1, strip.size - 1):
                strip.set_color(light_index + 1, self._average_colors(strip.get_color(light_index),strip.get_color(light_index + 1)))
            intensity = randint(0, 120)
            highlight = randint(0, 60)
            strip.set_color(0, RGBColor([intensity, highlight, highlight]))
            strip.set_color(strip.size - 1, self._average_colors(strip.get_color(strip.size - 1), self.OFF_COLOR))

    def _average_colors(self, a, b):
        r1, g1, b1 = a.rgb
        r2, g2, b2 = b.rgb

        return RGBColor([(r1 + r2) / 2, (g1 + g2) / 2, (b1 + b2) / 2])

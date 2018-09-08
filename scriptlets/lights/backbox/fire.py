from random import randint
from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Fire(DynamicBackBoxShow):
    OFF_COLOR = RGBColor([0, 0, 0])

    def __init__(self, machine):
        super().__init__(machine)

    def animate(self):
        super().animate()

        for strip in self.strips:
            # highlight = randint(0, 30)
            intensity = randint(0, 120)
            strip.set_color(strip.size - 1, RGBColor([intensity, intensity / 2, intensity / 4]))

            for light_index in reversed(range(1, strip.size)):
                strip.set_color(light_index - 1, self._decay_colors(strip.get_color(light_index), strip.get_color(light_index - 1)))

            strip.set_color(0, self._decay_colors(strip.get_color(0), self.OFF_COLOR))

    def _decay_colors(self, a, b):
        r1, g1, b1 = a.rgb
        r2, g2, b2 = b.rgb

        return RGBColor([(r1 + r2) / 2, (g1 + g2) / 2, (b1 + b2) / 2])

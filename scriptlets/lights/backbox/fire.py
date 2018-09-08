from random import randint
from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Fire(DynamicBackBoxShow):
    FIRE_COLOR = RGBColor([80, 35, 0])

    def __init__(self, machine):
        super().__init__(machine)

    def animate(self):
        super().animate()
        for strip in self.strips:
            for light_index in range(1, strip.size - 1):
                strip.set_color(light_index + 1, (strip.get_color(light_index) * 0.5 + strip.get_color(light_index + 1) * 0.5))
            strip.set_color(0, RGBColor([intensity, intensity / 2, intensity / 2])
            strip.set_color(strip.size - 1, strip.get_color(strip.size - 1) * 0.5)

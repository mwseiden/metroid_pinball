from random import randint
from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class Fire(DynamicBackBoxShow):
    FIRE_COLOR = RGBColor([80, 35, 0])

    def __init__(self):
        super().__init__(machine)

    def animate(self):
        super().animate()
        for strip in self.strips:
            for light_index in range(strip.size):
                intensity = randint(0, 80)
                strip.set_color((light_index, strip.get_color(light_index) + FIRE_COLOR) - RGBColor([intensity, intensity / 2, 0]))

from random import randint
from random import choice
from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import Plasma

class Fire(Plasma):
    FIRE_COLORS = [
        RGBColor([80, 80, 80]),
        RGBColor([80, 70, 60]),
        RGBColor([80, 60, 40]),
        RGBColor([80, 50, 20]),
        RGBColor([80, 40, 0]),
        RGBColor([80, 30, 0]),
        RGBColor([80, 20, 0]),
        RGBColor([80, 10, 0])
    ]

    def __init__(self, machine):
        super().__init__(machine, self.FIRE_COLORS, 1.8, 2.6, 3.2)

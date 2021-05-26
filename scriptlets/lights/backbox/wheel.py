from colorsys import hsv_to_rgb
from mpf.core.rgb_color import RGBColor

class Wheel:

    def at(self, wheel_pos):
        color = hsv_to_rgb(wheel_pos / 255, 1.0, 1.0)
        return RGBColor([int(color[0] * 255), int(color[1] * 255), int(color[2] * 255)])


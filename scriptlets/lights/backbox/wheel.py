from colorsys import hsv_to_rgb
from mpf.core.rgb_color import RGBColor

class Wheel:

    def at(self, wheel_pos):
        color = hsv_to_rgb(wheel_pos / 255, 1.0, 1.0)
        return RGBColor([int(color[0] * 255), int(color[1] * 255), int(color[2] * 255)])


    def at_old(self, wheel_pos):

        if wheel_pos < 85:
            return RGBColor([(wheel_pos * 3) % 255, 255 - (wheel_pos % 255), 0])
        elif wheel_pos < 170:
            wheel_pos -= 85;
            return RGBColor([255 - ((wheel_pos * 3) % 255), 0, (wheel_pos * 3) % 255])
        else:
            wheel_pos -= 170;
            return RGBColor([0, (wheel_pos * 3) % 255, 255 - ((wheel_pos * 3) % 255)])

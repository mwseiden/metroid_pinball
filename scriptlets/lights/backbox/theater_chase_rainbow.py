from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow

class TheaterChaseRainbow(DynamicBackBoxShow):

    def __init__(self, machine):
        super().__init__(machine)

        self.offset = 0
        self.q = 0
        self.j = 0

    def animate(self):
        super().animate()

        for strip_number in range(0, 11):
            i = 0
            while i < 10:
                self.strips[strip_number].set_color(i + self.q, self.wheel((i + self.j + strip_number) % 255)

        self.q += 1
        if self.q > 2:
            self.q = 0

        self.j += 1
        if self.j > 255:
            self.j = 0


    def wheel(self, wheel_pos):

        if wheel_pos < 85:
            return RGBColor(wheel_pos * 3, 255 - wheel_pos, 0)
        elif wheel_pos < 170:
            wheel_pos -= 85;
            return RGBColor(255 - wheel_pos * 3, 0, wheel_pos * 3)
        else:
            wheel_pos -= 170;
            return RGBColor(0, wheel_pos * 3, 255 - wheel_pos * 3)

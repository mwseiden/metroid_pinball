from mpf.core.rgb_color import RGBColor
from .dynamic_backbox_show import DynamicBackBoxShow
from .wheel import Wheel

class TheaterChaseRainbow(DynamicBackBoxShow):

    def __init__(self, machine, speed, spacing, increment):
        super().__init__(machine)

        self.offset = 0
        self.q = 0
        self.j = 0
        self.speed = speed
        self.spacing = spacing
        self.cycle_increment = increment
        self.wheel = Wheel()

    def animate(self):
        super().animate()

        if self.frame % self.speed == 0:
            self._update_lights()
            self._update_animation()


    def _update_lights(self):
        for strip_number in range(0, 10):
            i = 0
            while i < 10:
                if i % self.spacing == self.q:
                    self.strips[strip_number].set_color(i, self.wheel.at((i + self.j) % 255))
                else:
                    self.strips[strip_number].set_color(i, RGBColor([0, 0, 0]))
                i += 1


    def _update_animation(self):
        self.q += 1
        if self.q >= self.spacing:
            self.q = 0
            self.j += self.cycle_increment
            if self.j > 255:
                self.j = self.j % 255


    # def wheel(self, wheel_pos):

        # if wheel_pos < 85:
            # return RGBColor([(wheel_pos * 3) % 255, 255 - (wheel_pos % 255), 0])
        # elif wheel_pos < 170:
            # wheel_pos -= 85;
            # return RGBColor([255 - ((wheel_pos * 3) % 255), 0, (wheel_pos * 3) % 255])
        # else:
            # wheel_pos -= 170;
            # return RGBColor([0, (wheel_pos * 3) % 255, 255 - ((wheel_pos * 3) % 255)])

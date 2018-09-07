from .dynamic_backbox_show import DynamicBackBoxShow

class Solid(DynamicBackBoxShow):

    def __init__(self, machine, color):
        super().__init__(machine)

        self.color = color
        self.drawn = False

    def animate(self):
        super().animate()

        if not self.drawn:
            for strip in self.strips:
                strip.set_all_colors(self.color)
            self.drawn = True

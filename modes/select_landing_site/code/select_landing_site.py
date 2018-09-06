from mpf.modes.carousel.code.carousel import Carousel

class SelectLandingSite(Carousel):

    def mode_init(self):
        super().mode_init()

        player = self.machine.game.player
        if player['has_chosen_landing_site'] != 0:
            self._items.insert(0, 'continue')
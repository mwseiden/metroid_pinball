from mpf.modes.carousel.code.carousel import Carousel

class SelectLandingSite(Carousel):

    def _update_highlighted_item(self, direction):
        player = self.machine.game.player
        items = self._get_available_items()

        if player['has_chosen_landing_site'] != 0 and direction is None:
            items.insert(0, 'continue')

        super()._update_highlighted_item(direction)

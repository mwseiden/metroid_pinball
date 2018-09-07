from mpf.modes.carousel.code.carousel import Carousel

class SelectLandingSite(Carousel):

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)

        self._register_handlers('select_landing_site_continue_selected', self._continue_from_last_room)

    def _update_highlighted_item(self, direction):
        player = self.machine.game.player
        items = self._get_available_items()

        if player['has_chosen_landing_site'] != 0 and 'continue' not in items:
            items.insert(0, 'continue')

        super()._update_highlighted_item(direction)

    def _continue_from_last_room(self):
        player = self.machine.game.player
        self.machine.events.post('room_{}_continue'.format(player['continue_room']))

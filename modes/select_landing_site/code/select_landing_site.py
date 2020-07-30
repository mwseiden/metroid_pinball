from random import randint
from mpf.modes.carousel.code.carousel import Carousel

class SelectLandingSite(Carousel):

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)

        self.add_mode_event_handler('select_landing_site_continue_selected', self._continue_from_last_room)
        self.add_mode_event_handler('select_landing_site_continue_highlighted', self._show_continue_map)

    def _update_highlighted_item(self, direction):
        player = self.machine.game.player
        items = self._get_available_items()

        if player['has_chosen_landing_site'] != 0 and 'continue' not in items:
            items.insert(0, 'continue')

        if player.number == 1 and player.ball == 1:
            self.machine.set_machine_var('current_game_default_mode', randint(0, len(items)))

        if player.ball == 1:
            self._highlighted_item_index = self.machine.get_machine_var('current_game_default_mode')

        super()._update_highlighted_item(direction)

    def _continue_from_last_room(self, **kwargs):
        player = self.machine.game.player
        player['last_continue_room'] = player['continue_room']
        self.machine.events.post('room_{}_continue'.format(player['continue_room']))

    def _show_continue_map(self, **kwargs):
        self.machine.modes.map.event_set_location(room=self.machine.game.player['continue_room'])

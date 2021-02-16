from mpf.core.mode import Mode

class Scoop(Mode):

    def mode_start(self, **kwargs):
        self.add_mode_event_handler('ball_hold_collect_award_shot_held_ball', self.event_ball_collected)
        self.add_mode_event_handler('cmd_scoop_collect', self.event_scoop_hold_collect)
        # self.add_mode_event_handler('cmd_scoop_clear', self.event_scoop_clear)

        super().mode_start(**kwargs)


    def event_ball_collected(self, **kwargs):
        player = self.machine.game.player

        if player['scoop_collectables'][0] == '1':
            self.machine.events.post('scoop_award_land_the_gunship')
            self._clear_collectable(0)

        self.machine.events.post('scoop_award_collected')

    def event_scoop_hold_collect(self, **kwargs):
        self._set_collectable(kwargs.get('index', 0))

    def event_scoop_clear(self, **kwargs):
        self._clear_collectable(kwargs.get('index', 0))

    def _set_collectable(self, index):
        self.machine.game.player['scoop_collectables'] = player[:index] + '1' + string[index+1:]

    def _clear_collectable(self, index):
        self.machine.game.player['scoop_collectables'] = player[:index] + '0' + string[index+1:]

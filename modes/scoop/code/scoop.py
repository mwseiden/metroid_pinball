from mpf.core.mode import Mode

class Scoop(Mode):

    def mode_start(self, **kwargs):
        self.add_mode_event_handler('ball_hold_collect_award_shot_held_ball', self.event_ball_collected)
        self.add_mode_event_handler('cmd_scoop_collect', self.event_scoop_hold_collect)
        self.add_mode_event_handler('cmd_advance_scoop_indicator', self.event_scoop_advance_indicator)

        super().mode_start(**kwargs)


    def event_ball_collected(self, **kwargs):
        player = self.machine.game.player

        if player['scoop_collectables'][0] == '1':
            self.machine.events.post('scoop_award_land_the_gunship')
            self._clear_collectable(0)
        elif player['scoop_collectables'][1] == '1':
            self.machine.events.post('scoop_award_side_targets')
            self._clear_collectable(1)
        else:
          self.machine.events.post('scoop_ball_hold_release')

        self.machine.events.post('cmd_advance_scoop_indicator')

    def event_scoop_hold_collect(self, **kwargs):
        self._set_collectable(kwargs.get('index', 0))
        self.machine.events.post('scoop_collect_enable')
        self.machine.events.post('scoop_award_available_to_collect')

    def event_scoop_advance_indicator(self, **kwargs):
        player = self.machine.game.player
        index = player['scoop_indicator_index']
        new_index = 0

        show = None

        for i in range(index + 1, 8):
          if player['scoop_collectables'][i] == '1':
            show = self._get_show(i)
            if show is not None:
              new_index = i
            break

        if show is None:
          for i in range(0, index):
            show = self._get_show(i)
            if show is not None:
              new_index = i
            break

        if show is None:
          show = 'none'

        new_index = new_index + 1

        if new_index > 7:
          new_index = 0

        self.machine.events.post('scoop_play_lights_{}'.format(show))

        player['scoop_indicator_index'] = new_index

    def _get_show(self, i):
        if i == 0:
          return 'collect_gunship'
        elif i == 1:
          return 'side_targets'
        else:
          return None


    def _set_collectable(self, index):
        collectables = self.machine.game.player['scoop_collectables']
        self.machine.game.player['scoop_collectables'] = collectables[:index] + '1' + collectables[index+1:]

    def _clear_collectable(self, index):
        collectables = self.machine.game.player['scoop_collectables']
        self.machine.game.player['scoop_collectables'] = collectables[:index] + '0' + collectables[index+1:]

from mpf.core.mode import Mode

class Scoop(Mode):

    COLLECT_EVENTS = [
      'scoop_award_land_the_gunship',
      'cmd_map_call_gunship', # 'scoop_award_side_targets',
      'scoop_award_miniboss'
    ]

    def mode_start(self, **kwargs):
        self.add_mode_event_handler('ball_hold_collect_award_shot_held_ball', self.event_ball_collected)
        self.add_mode_event_handler('cmd_scoop_check_for_award', self.event_scoop_check_for_award)
        self.add_mode_event_handler('cmd_scoop_collect', self.event_scoop_hold_collect)
        self.add_mode_event_handler('cmd_scoop_collect_clear', self.event_scoop_collect_clear)
        self.add_mode_event_handler('cmd_scoop_collect_next', self.event_ball_collected)
        self.add_mode_event_handler('cmd_advance_scoop_indicator', self.event_scoop_advance_indicator)

        super().mode_start(**kwargs)


    def event_ball_collected(self, **kwargs):
        player = self.machine.game.player
        something_was_awarded = False

        for i in range(3):
            if player['scoop_collectables'][i] == '1' and self._collect_is_available(i):
                self.machine.events.post(self.COLLECT_EVENTS[i])
                self._clear_collectable(i)
                something_was_awarded = True
                break

        if not something_was_awarded:
            self.machine.events.post('scoop_ball_hold_release')

        # if player['scoop_collectables'][0] == '1':
            # self.machine.events.post('scoop_award_land_the_gunship')
            # self._clear_collectable(0)
        # elif player['scoop_collectables'][1] == '1':
            # self.machine.events.post('scoop_award_side_targets')
            # #self.machine.events.post('cmd_map_call_gunship')
            # self._clear_collectable(1)
        # elif player['scoop_collectables'][2] == '1' and self._collect_is_available(2):
            # self.machine.events.post('scoop_award_miniboss')
            # self._clear_collectable(2)
        # else:
          # self.machine.events.post('scoop_ball_hold_release')

        self.machine.events.post('cmd_advance_scoop_indicator')

    def event_scoop_hold_collect(self, **kwargs):
        self._set_collectable(kwargs.get('index', 0))
        self.machine.events.post('scoop_collect_enable')
        self.machine.events.post('cmd_advance_scoop_indicator')

    def event_scoop_advance_indicator(self, **kwargs):
        self._advance_indicator()

    def event_scoop_collect_clear(self, **kwargs):
        self._clear_collectable(kwargs.get('index', 0))

    def event_scoop_check_for_award(self, **kwargs):
        self._check_for_award()


    def _check_for_award(self):
        if self._find_next_index() is not None:
          self.machine.events.post('scoop_collect_enable')
          self.machine.events.post('cmd_advance_scoop_indicator')

    def _advance_indicator(self):
        player = self.machine.game.player
        index = self._find_next_index()

        if index is None:
          self.machine.events.post('scoop_stop_lights')
          player['scoop_indicator_index'] = 0
        else:
          show = self._get_show(index)
          self.machine.events.post('scoop_play_lights_{}'.format(show))
          player['scoop_indicator_index'] = index


    def _find_next_index(self):
        player = self.machine.game.player
        i = player['scoop_indicator_index']

        for i in range(i + 1, 8):
            if player['scoop_collectables'][i] == '1' and self._collect_is_available(i):
                return i

        for i in range(0, i):
            if player['scoop_collectables'][i] == '1' and self._collect_is_available(i):
                return i

        return None

    def _get_show(self, i):
        if i == 0:
          return 'collect_gunship'
        elif i == 1:
          return 'side_targets'
        elif i == 2:
          return 'miniboss'
        else:
          return 'none'


    def _set_collectable(self, index):
        collectables = self.machine.game.player['scoop_collectables']
        self.machine.game.player['scoop_collectables'] = collectables[:index] + '1' + collectables[index+1:]

    def _clear_collectable(self, index):
        collectables = self.machine.game.player['scoop_collectables']
        self.machine.game.player['scoop_collectables'] = collectables[:index] + '0' + collectables[index+1:]

    def _is_multiball(self):
        return self.machine.game.balls_in_play > 1 or self._is_generator_running()

    def _is_generator_running(self):
        generator_state = self.machine.sequences['room_1m_generator_sequence'].value
        return (generator_state is None or generator_state < 2) and self.player['continue_room'] == '1m'

    def _collect_is_available(self, index):
        return not self._is_multiball() or (self._is_multiball() and index in [0])

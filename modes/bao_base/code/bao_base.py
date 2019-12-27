from random import randint
from mpf.core.mode import Mode

class BaoBase(Mode):

    def mode_start(self, **kwargs):
        self.info_log('Initializing BAO Base')

        self.add_mode_event_handler('bao_base_lock_a_ball', self.event_add_a_ball)
        self.add_mode_event_handler('bao_base_release_locked_balls', self.event_release_locked_balls)
        self.add_mode_event_handler('bao_base_initialize', self.event_initialize)
        self.add_mode_event_handler('bao_enable_stage_4', self.event_pick_shots)
        self.add_mode_event_handler('balldevice_bd_trough_ball_count_changed', self.event_check_for_end)
        self.add_mode_event_handler('bao_standard_shot_group_hit', self.event_play_rando_sound)
        self.add_mode_event_handler('bao_final_shot_completed', self.event_update_reactor_destroyed)
        self.add_mode_event_handler('bao_critical_should_start', self.event_update_reactor_started)

        super().mode_start(**kwargs)

    def event_add_a_ball(self, **kwargs):
        self.machine.set_machine_var('bao_balls_locked', self.machine.get_machine_var('bao_balls_locked') + 1)
        self.machine.playfield.add_ball()

    def event_release_locked_balls(self, **kwargs):
        self.machine.set_machine_var('bao_balls_locked', 0)
        self.machine.game.balls_in_play += 2

    def event_initialize(self, **kwargs):
        self.machine.set_machine_var('bao_balls_locked', 0)

    def event_pick_shots(self, **kwargs):
        self.machine.events.post('bao_enable_final_shot_' + str(randint(1, 6)))

    def event_check_for_end(self, **kwargs):
        if int(kwargs.get('balls', 3)) >= 3:
            self.machine.events.post('bao_multiball_ended')

    def event_play_rando_sound(self, **kwargs):
        if (randint(0, 12) == 0):
            self.machine.events.post('bao_play_rare')
        else:
            self.machine.events.post('bao_play_standard')

    def event_update_reactor_started(self, **kwargs):
        player = self.machine.game.player
        self.machine.events.post('bao_reactor_{}_started'.format(player['bao_reactors'] + 1))

    def event_update_reactor_destroyed(self, **kwargs):
        player = self.machine.game.player
        self.machine.events.post('bao_reactor_{}_destroyed'.format(player['bao_reactors'] + 1))
        self.machine.events.post('bao_update_reactor_count')

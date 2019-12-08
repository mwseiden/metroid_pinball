from mpf.core.mode import Mode

class BaoBase(Mode):

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)

        self.add_mode_event_handler('bao_base_lock_a_ball', self.event_add_a_ball)
        self.add_mode_event_handler('bao_base_release_locked_balls', self.event_release_locked_balls)

    def event_add_a_ball(self, **kwargs):
        self.machine.set_machine_var('bao_balls_locked', self.machine.get_machine_var('bao_balls_locked') + 1)
        self.machine.playfield.add_ball()

    def event_release_locked_balls(self, **kwargs):
        self.machine.set_machine_var('bao_balls_locked', 0)
        self.machine.game.balls_in_play += 2

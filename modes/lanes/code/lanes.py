from mpf.core.mode import Mode

class Lanes(Mode):

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)

        self.add_mode_event_handler('left_ballsave_shot_hit', self.event_add_a_ball)
        self.add_mode_event_handler('right_ballsave_shot_hit', self.event_add_a_ball)

    def event_add_a_ball(self, **kwargs):
        self.machine.playfield.add_ball()
        self.machine.game.balls_in_play += 1


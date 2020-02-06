from mpf.core.mode import Mode

class Lanes(Mode):

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)

        self.add_mode_event_handler('left_ballsave_shot_hit', self.event_add_a_ball)
        self.add_mode_event_handler('right_ballsave_shot_hit', self.event_add_a_ball)
        self.add_mode_event_handler('lanes_collect_ball_save', self.event_add_a_ball)

    def event_add_a_ball(self, **kwargs):
        for ball_save in self.machine.ball_saves:
            if ball_save.enabled:
                return

        self.player.lanes_last_shot = 0

        if self.machine.game.balls_in_play < 4:
            self.machine.game.balls_in_play += 1
            self.machine.playfield.add_ball()
            self.player.kickbacks -= 1
            self.machine.events.post('lanes_ball_was_saved')


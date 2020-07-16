from mpf.core.mode import Mode

class Base(Mode):

    def mode_start(self, **kwargs):
        if self.machine.ball_devices['bd_trough'].available_balls == 4:
            self.machine.playfield.available_balls = 0

        super().mode_start(**kwargs)

    def mode_stop(self, **kwargs):
        super().mode_stop(**kwargs)

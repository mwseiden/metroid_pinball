from mpf.modes.attract.code.attract import Attract
import time

class MyAttract(Attract):
    DOUBLE_FLIP_MILLIS = 250

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)

        self.flip_pattern = ''
        self.set_last_flipper_hit()

        self.add_mode_event_handler('switch_s_right_flipper_active', self.right_flipper_down)
        self.add_mode_event_handler('switch_s_right_flipper_inactive', self.right_flipper_up)
        self.add_mode_event_handler('switch_s_left_flipper_active', self.left_flipper_down)
        self.add_mode_event_handler('switch_s_left_flipper_inactive', self.left_flipper_up)

    def right_flipper_down(self, **kwargs):
        self.right_flipper_down = true

    def right_flipper_up(self, **kwargs):
        self.right_flipper_down = false
        self.handle_flipper_hit(self.left_flipper_down, 'R')

    def left_flipper_down(self, **kwargs):
        self.left_flipper_down = true

    def left_flipper_up(self, **kwargs):
        self.left_flipper_down = false
        self.handle_flipper_hit(self.right_flipper_down, 'L')

    def get_last_flipper_hit(self):
        return self.current_time() - self.last_hit_time

    def set_last_flipper_hit(self):
        self.last_hit_time = self.current_time()

    def current_time(self):
        return int(round(time.time() * 1000))

    def log_flipper_code(self):
        info_log('Flipper Code: %s', self.flip_pattern)

    def handle_flipper_hit(self, opposite_flipper_state, token):
        if self.opposite_flipper_state:
            self.flip_pattern = 'B'
        elif self.flip_pattern != 'B' or self.get_last_flipper_hit() > self.DOUBLE_FLIP_MILLIS:
            self.flip_pattern += token

        self.set_last_flipper_hit()
        self.log_flipper_code()
        self.check_flipper_code()

    def check_flipper_code(self):
        if self.flip_pattern == 'BLRRLLL':
            info_log('Flipper Code: LORD SQUEEK')

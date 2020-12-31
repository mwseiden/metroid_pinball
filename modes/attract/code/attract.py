from random import randint
from mpf.modes.attract.code.attract import Attract
from mpf.core.rgb_color import RGBColor
import time

class MyAttract(Attract):
    DOUBLE_FLIP_MILLIS = 250

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)

        self.flip_pattern = ''
        self.set_last_flipper_hit()
        self.right_flipper_down = False
        self.left_flipper_down = False

        self.add_mode_event_handler('s_right_flipper_active', self.event_right_flipper_down)
        self.add_mode_event_handler('s_right_flipper_inactive', self.event_right_flipper_up)
        self.add_mode_event_handler('s_left_flipper_active', self.event_left_flipper_down)
        self.add_mode_event_handler('s_left_flipper_inactive', self.event_left_flipper_up)
        self.add_mode_event_handler('attract_play_message', self.event_play_message_show)

        self.machine.set_machine_var('metroid_game_booted', 1)
        self.machine.set_machine_var('next_game_acapella', 0)
        self.machine.set_machine_var('next_game_bao', 0)
        self.machine.set_machine_var('next_game_goren', 0)
        self.machine.set_machine_var('next_game_macho', 0)
        self.machine.set_machine_var('bao_balls_locked', 0)

    def event_play_message_show(self, **kwargs):
        settings = {
          'attract_message_{}'.format(randint(1, 4)): {
            'loops': 0,
            'action': 'play',
            'block_queue': False
          }
        }

        self.machine.show_player.play(settings, 'attract', None)

    def event_right_flipper_down(self, **kwargs):
        self.right_flipper_down = True

    def event_right_flipper_up(self, **kwargs):
        self.right_flipper_down = False
        self.handle_flipper_hit(self.left_flipper_down, 'R')

    def event_left_flipper_down(self, **kwargs):
        self.left_flipper_down = True

    def event_left_flipper_up(self, **kwargs):
        self.left_flipper_down = False
        self.handle_flipper_hit(self.right_flipper_down, 'L')

    def get_last_flipper_hit(self):
        return self.current_time() - self.last_hit_time

    def set_last_flipper_hit(self):
        self.last_hit_time = self.current_time()

    def current_time(self):
        return int(round(time.time() * 1000))

    def log_flipper_code(self):
        self.info_log('Flipper Code: %s', self.flip_pattern)

    def handle_flipper_hit(self, opposite_flipper_state, token):
        if opposite_flipper_state:
            self.flip_pattern = 'B'
        elif self.flip_pattern != 'B' or self.get_last_flipper_hit() > self.DOUBLE_FLIP_MILLIS:
            self.flip_pattern += token

        self.set_last_flipper_hit()
        self.log_flipper_code()
        self.check_flipper_code()

    def check_flipper_code(self):
        if self.flip_pattern == 'BLRRLLL':
            self.info_log('Flipper Code: LORD SQUEAK')
            self.machine.events.post('flipper_code_squeak')
        elif self.flip_pattern == 'BLLRRRLLLL':
            self.info_log('Flipper Code: NO MUSIC')
            self.machine.events.post('flipper_code_no_music')
            self.machine.set_machine_var('next_game_acapella', 1)
        elif self.flip_pattern == 'BLLRLLLLLLLLLLLLLLL':
            self.info_log('Flipper Code: BAO')
            self.machine.events.post('flipper_code_bao')
            self.machine.set_machine_var('next_game_bao', 1)
        elif self.flip_pattern == 'BLRRRRRRRRLRRRRRRRR':
            self.info_log('Flipper Code: Goren')
            self.machine.events.post('flipper_code_goren')
            self.machine.set_machine_var('next_game_goren', 1)
            self.machine.set_machine_var('next_game_macho', 0)
        elif self.flip_pattern == 'BLLLLLLLLLLLLLLLLLLLLLLLLLRRRRRL':
            self.info_log('Flipper Code: Macho')
            self.machine.events.post('flipper_code_macho')
            self.machine.set_machine_var('next_game_goren', 0)
            self.machine.set_machine_var('next_game_macho', 1)

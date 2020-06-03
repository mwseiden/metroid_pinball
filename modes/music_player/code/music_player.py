from mpf.core.mode import Mode

class MusicPlayer(Mode):

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)
        self.add_mode_event_handler('cmd_play_music', self.event_play_music)
        self.add_mode_event_handler('cmd_stop_music', self.event_stop_music)
        self.current_music = 'item_room'

    def mode_stop(self, **kwargs):
        super().mode_stop(**kwargs)

    def event_play_music(self, **kwargs):
        if self.machine.get_machine_var('next_game_acapella') != 0:
            return None

        new_music = kwargs.get('music', 'item_room')

        if new_music != self.current_music:
            self.stop_music('1s')

        settings = {
          'music_{}'.format(new_music): {
            'action': 'play',
            'loops': -1
          }
        }

        self.machine.sound_player.play(settings, 'music_player', None)

        self.current_music = new_music

    def event_stop_music(self, **kwargs):
        self.stop_music('3s')

    def stop_music(self, fade_out):
        settings = {
          'music_{}'.format(self.current_music): {
            'action': 'stop',
            'fade_out': fade_out
          }
        }

        self.machine.sound_player.play(settings, 'music_player', None)

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
        music = kwargs.get('music', 'item_room')

        if music != self.music:
            self.stop_music('1s')

        settings = {
          'music_{}'.format(music): {
            'action': 'play',
            'loops': -1
          }
        }

        self.machine.sound_player.play(settings, 'music_player', None)

        self.music = music

    def event_stop_music(self, **kwargs):
        self.stop_music('3s')

    def stop_music(self, fade_out):
        settings = {
          'music_{}'.format(self.music): {
            'action': 'stop',
            'fade_out': fade_out
          }
        }

        self.machine.sound_player.play(settings, 'music_player', None)

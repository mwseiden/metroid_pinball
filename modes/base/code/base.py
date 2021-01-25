from random import randint
from mpf.core.mode import Mode

class Base(Mode):

    def mode_start(self, **kwargs):
        self.current_music = None
        self.current_overlay_music = None

        self.add_mode_event_handler('cmd_play_map_music', self.event_play_map_music)
        self.add_mode_event_handler('cmd_play_overlay_music', self.event_play_overlay_music)
        self.add_mode_event_handler('cmd_stop_all_music', self.event_stop_all_music)
        self.add_mode_event_handler('cmd_stop_map_music', self.event_stop_map_music)
        self.add_mode_event_handler('cmd_stop_overlay_music', self.event_stop_overlay_music)

        super().mode_start(**kwargs)

    def event_play_map_music(self, **kwargs):
        music = kwargs.get('music', None)

        if self.current_music != music:
            self.stop_map_music()
            self.play_map_music(music)

    def event_play_overlay_music(self, **kwargs):
        self.stop_overlay_music()
        self.play_overlay_music(kwargs.get('music', None))

    def event_stop_all_music(self, **kwargs):
        self.stop_map_music()

        if self.current_overlay_music is not None:
            self._stop_music(self.current_overlay_music)
            self.current_overlay_music = None

    # should be temporary
    def event_stop_map_music(self, **kwargs):
        self.stop_map_music()

    def event_stop_overlay_music(self, **kwargs):
        self.stop_overlay_music()

    def stop_map_music(self):
        if self.current_music is not None:
            self._stop_music(self.current_music)
            self.current_music = None

    def play_map_music(self, music):
        self.current_music = music

        if self.current_music is not None and self.current_overlay_music is None:
            self._play_music(self.current_music)

    def stop_overlay_music(self):
        if self.current_overlay_music is not None:
            self._stop_music(self.current_overlay_music)
            self.current_overlay_music = None
            self.play_map_music(self.current_music)

    def play_overlay_music(self, music):
        if self.current_music is not None:
            self._stop_music(self.current_music)

        self.current_overlay_music = music

        if self.current_overlay_music is not None:
            self._play_music(self.current_overlay_music)


    def _stop_music(self, music):
        if self._music_enabled():
            settings = {
                music: {
                    'action': 'stop',
                    'fade_out': '1s',
                }
            }

            self.machine.sound_player.play(settings, 'base', None)

    def _play_music(self, music):
        if self._music_enabled():
            settings = {
                music: {
                    'action': 'play',
                    'fade_in': '1s',
                }
            }

            self.machine.sound_player.play(settings, 'base', None)

    def _music_enabled(self):
        return self.machine.get_machine_var('next_game_acapella') == 0

from random import randint
from mpf.core.mode import Mode

class Boss(Mode):

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)

        self.add_mode_event_handler('timer_boss_exploder_timer_tick', self.event_boss_explode)
        self.add_mode_event_handler('timer_boss_exploder_timer_complete', self.event_boss_explode_done)

    def event_boss_explode(self, **kwargs):
        self._remove_explode()
        self._show_explode()

    def event_boss_explode_done(self, **kwargs):
        self._remove_explode()

    def _show_explode(self):
        settings = {
          'boss_explosion_widget': {
            'action': 'add',
            'target': 'backglass',
            'key': 'boss_explosion_widget',
            'fps': 25,
            'widget_settings': {
              'x': randint(128, 592),
              'y': randint(256, 900),
              'z': 1000,
            }
          }
        }

        self.machine.widget_player.play(settings, 'boss', None)

    def _remove_explode(self):
        settings = {
          'boss_explosion_widget': {
            'action': 'remove',
            'target': 'backglass',
            'key': 'boss_explosion_widget',
          }
        }

        self.machine.widget_player.play(settings, 'boss', None)

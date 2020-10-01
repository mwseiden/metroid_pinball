from random import randint
from mpf.core.mode import Mode

class Boss(Mode):

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)

        self.add_mode_event_handler('boss_explode', self.event_boss_explode)
        self.add_mode_event_handler('boss_explode_done', self.event_boss_explode_done)

    def event_boss_explode(self, **kwargs):
        self._remove_explode()
        self._show_explode(randint(128, 592), randint(256, 900))

    def event_boss_explode_done(self, **kwargs):
        self._remove_explode()

    def _show_explode(self, x, y):
        settings = {
          'boss_explosion_widget': {
            'action': 'add',
            'target': 'backglass',
            'key': 'boss_explosion_widget',
            'fps': 25,
            'widget_settings': {
              'x': x,
              'y': y,
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

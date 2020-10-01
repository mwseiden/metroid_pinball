from mpf.core.mode import Mode

class Boss(Mode):

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)

        self.add_mode_event_handler('boss_explode', self.event_boss_explode)

    def event_boss_explode(self, **kwargs):
        self._remove_explode()
        self._show_explode(0, 0)

    def _show_explode(self, x, y):
        settings = {
          'boss_explosion_widget': {
            'action': 'add',
            'target': 'backglass',
            'key': 'boss_explosion_widget',
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

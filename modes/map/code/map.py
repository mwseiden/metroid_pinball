from mpf.core.mode import Mode

class Map(Mode):

    ORIGIN_X = 505
    ORIGIN_Y = 905

    LAYOUT = {
      'C': {
        '1b': [1, 0, 0, 0, None, 1, None, 1, None, 0, None]
      }
    }

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)
        self.add_mode_event_handler('cmd_map_position', self.event_set_location)

    def mode_stop(self, **kwargs):
        super().mode_stop(**kwargs)

    def event_set_location(self, **kwargs):
        self.remove_room(1)
        settings = {
          'map_tile_1': {
            'action': 'add',
            'target': 'window',
            'key': 'map_room_1',
            'widget_settings': {
              'x': self.ORIGIN_X,
              'y': self.ORIGIN_Y,
              'z': 1001,
              'image': 'map_tile_undiscovered'
            }
          }
        }

        self.info_log('WTF 1')
        self.machine.widget_player.play(settings, 'map', None)
        self.info_log('WTF 2')

    def remove_room(self, room_number):
        settings = {
          'map_tile_1': {
            'action': 'remove',
            'target': 'window',
            'key': 'map_room_1'
          }
        }

        self.info_log('WTF 3')
        self.machine.widget_player.play(settings, 'map', None)
        self.info_log('WTF 4')
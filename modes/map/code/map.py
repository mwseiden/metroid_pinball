from mpf.core.mode import Mode

class Map(Mode):

    ORIGIN_X = 688
    ORIGIN_Y = 1024

    # door types:
    # 0: None
    # 1: Blue
    # 2: Red - Missile
    # 3: Green - Power Bomb
    # 4: Area Exit

    # door order: N - E - W - S

    LAYOUT = {
      '1a': ['c', 1, 1, 0, 0, None, 1, None, 0, None, 2, 'door_1a_1f'],
      '1b': ['c', 2, 2, 0, 0, None, 1, None, 0, None, 0, None],
      '1c': ['c', 3, 3, 0, 0, None, 1, None, 0, None, 4, None],
      '1d': ['c', 4, 4, 0, 0, None, 4, None, 0, None, 0, None],
      '1e': ['c', 5, 0, 1, 0, None, 1, None, 4, None, 0, None],
      '1f': ['c', 6, 1, 1, 0, None, 1, None, 1, None, 4, None],
      '1g': ['c', 7, 2, 1, 0, None, 1, None, 0, None, 0, None]
    }

    AREAS = {
      'c': [192, 96, ['1a', '1b', '1c', '1d', '1e', '1f', '1g']]
    }

    DOOR_TYPES = {
      0: 'none',
      1: 'blue',
      2: 'red',
      3: 'green',
      4: 'area'
    }

    DOOR_DIRECTIONS = {
      'n': 'v',
      'e': 'h',
      'w': 'h',
      's': 'v'
    }

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)
        self.add_mode_event_handler('cmd_map_position', self.event_set_location)

    def mode_stop(self, **kwargs):
        super().mode_stop(**kwargs)

    def event_set_location(self, **kwargs):
        room_code = kwargs.get('room', '1b')

        if kwargs.get('visit', False):
            player_var = 'map_visited_{}'.format(self.LAYOUT[room_code][0])
            current_visits = list(self.player[player_var])
            current_visits[self.LAYOUT[room_code][1] - 1] = 'Y'
            self.player[player_var] = "".join(current_visits)

        self.player.map_location = room_code
        self.draw_map('c')

    def draw_map(self, area_code):
        self.remove_background()
        self.draw_background(area_code)

        self.remove_player()

        for room_code in self.AREAS[area_code][2]:
            self.draw_map_tile(room_code)

    def draw_map_tile(self, room_code):
        area_code, room_number, x, y, exit_n_type, exit_n_var, exit_e_type, exit_e_var, exit_w_type, exit_w_var, exit_s_type, exit_s_var = self.LAYOUT.get(room_code)

        x = self.ORIGIN_X - self.AREAS[area_code][0] + 24 + (x * 32)
        y = self.ORIGIN_Y - 24 - (y * 32)

        self.remove_room(room_number)
        self.remove_exit(room_number, 'n')
        self.remove_exit(room_number, 'e')
        self.remove_exit(room_number, 'w')
        self.remove_exit(room_number, 's')

        self.draw_room(room_number, x, y, list(self.player['map_visited_{}'.format(self.LAYOUT[room_code][0])])[room_number - 1] == 'Y')
        self.draw_exit(room_number, 'n', x, y + 14, exit_n_type, exit_n_var)
        self.draw_exit(room_number, 'e', x + 14, y, exit_e_type, exit_e_var)
        self.draw_exit(room_number, 'w', x - 14, y, exit_w_type, exit_w_var)
        self.draw_exit(room_number, 's', x, y - 14, exit_s_type, exit_s_var)

        if self.player.map_location == room_code:
            self.draw_player(x, y)

    def draw_background(self, area_code):
        settings = {
          'map_background_widget': {
            'action': 'add',
            'target': 'window',
            'key': 'map_background_widget',
            'widget_settings': {
              'x': self.ORIGIN_X - (self.AREAS[area_code][0] / 2),
              'y': self.ORIGIN_Y - (self.AREAS[area_code][1] / 2),
              'z': 1000,
              'width': self.AREAS[area_code][0],
              'height': self.AREAS[area_code][1]
            }
          }
        }

        self.machine.widget_player.play(settings, 'map', None)

    def remove_background(self):
        settings = {
          'map_background_widget': {
            'action': 'remove',
            'target': 'window',
            'key': 'map_background_widget'
          }
        }

        self.machine.widget_player.play(settings, 'map', None)

    def draw_room(self, room_number, x, y, room_type):
        settings = {
          'map_tile_{}'.format(room_number): {
            'action': 'add',
            'target': 'window',
            'key': 'map_room_{}'.format(room_number),
            'widget_settings': {
              'x': x,
              'y': y,
              'z': 1001,
              'image': 'map_tile_discovered' if room_type else 'map_tile_undiscovered'
            }
          }
        }

        self.machine.widget_player.play(settings, 'map', None)

    def remove_room(self, room_number):
        settings = {
          'map_tile_{}'.format(room_number): {
            'action': 'remove',
            'target': 'window',
            'key': 'map_room_{}'.format(room_number)
          }
        }

        self.machine.widget_player.play(settings, 'map', None)

    def draw_exit(self, room_number, exit_direction, x, y, exit_type, exit_var):
        if exit_type == 0:
            return

        settings = {
          'map_exit_{}_{}'.format(room_number, exit_direction): {
            'action': 'add',
            'target': 'window',
            'key': 'map_exit_{}_{}'.format(room_number, exit_direction),
            'widget_settings': {
              'x': x,
              'y': y,
              'z': 1001,
              'image': 'map_exit_{}_{}'.format(self.DOOR_TYPES[exit_type], self.DOOR_DIRECTIONS[exit_direction])
            }
          }
        }

        self.machine.widget_player.play(settings, 'map', None)

    def remove_exit(self, room_number, exit_direction):
        settings = {
          'map_exit_{}_{}'.format(room_number, exit_direction): {
            'action': 'remove',
            'target': 'window',
            'key': 'map_exit_{}_{}'.format(room_number, exit_direction)
          }
        }

        self.machine.widget_player.play(settings, 'map', None)

    def draw_player(self, x, y):
        settings = {
          'map_player': {
            'action': 'add',
            'target': 'window',
            'key': 'map_player',
            'widget_settings': {
              'x': x,
              'y': y,
              'z': 1002,
              'image': 'map_player'
            }
          }
        }

        self.machine.widget_player.play(settings, 'map', None)

    def remove_player(self):
        settings = {
          'map_player': {
            'action': 'remove',
            'target': 'window',
            'key': 'map_player'
          }
        }

        self.machine.widget_player.play(settings, 'map', None)

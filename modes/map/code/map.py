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
      '1a': ['c', 1, 0, 1, 0, 0, None, 1, None, 0, None, 2, 'door_1a_1f'],
      '1b': ['c', 2, 0, 2, 0, 0, None, 1, None, 0, None, 0, None],
      '1c': ['c', 3, 0, 3, 0, 0, None, 1, None, 0, None, 4, None],
      '1d': ['c', 4, 0, 4, 0, 0, None, 4, None, 0, None, 0, None],
      '1e': ['c', 5, 0, 0, 1, 0, None, 1, None, 4, None, 0, None],
      '1f': ['c', 6, 0, 1, 1, 0, None, 1, None, 1, None, 4, None],
      '1g': ['c', 7, 0, 2, 1, 0, None, 0, None, 0, None, 0, None],

      '1h': ['w', 1, 0, 0, 0, 0, None, 1, None, 0, None, 0, None],
      '1i': ['w', 2, 0, 1, 0, 0, None, 1, None, 0, None, 1, None],
      '1j': ['w', 3, 1, 2, 0, 0, None, 0, None, 0, None, 0, None],
      '1k': ['w', 4, 0, 1, 1, 0, None, 0, None, 0, None, 1, None],
      '1l': ['w', 5, 0, 1, 2, 0, None, 1, None, 4, None, 1, None],
      '1m': ['w', 6, 0, 2, 2, 0, None, 0, None, 0, None, 0, None],
      '1n': ['w', 7, 0, 1, 3, 0, None, 0, None, 0, None, 1, None],
      '1o': ['w', 8, 0, 0, 4, 0, None, 1, None, 0, None, 0, None],
      '1p': ['w', 9, 0, 1, 4, 0, None, 1, None, 0, None, 0, None],
      '1q': ['w', 10, 0, 2, 4, 0, None, 0, None, 0, None, 4, None],

      '1r': ['b', 1, 0, 1, 0, 4, None, 1, None, 0, None, 1, None],
      '1s': ['b', 2, 0, 2, 0, 0, None, 1, None, 0, None, 0, None],
      '1t': ['b', 3, 0, 3, 0, 4, None, 0, None, 0, None, 1, None],
      '1u': ['b', 4, 0, 1, 1, 0, None, 0, None, 0, None, 1, None],
      '1v': ['b', 5, 0, 3, 1, 0, None, 0, None, 0, None, 1, None],
      '1w': ['b', 6, 0, 1, 2, 0, None, 1, None, 0, None, 0, None],
      '1x': ['b', 7, 1, 2, 2, 0, None, 1, None, 0, None, 0, None],
      '1y': ['b', 8, 0, 3, 2, 0, None, 4, None, 0, None, 0, None],

      '1z': ['m', 1, 0, 1, 0, 0, None, 1, None, 0, None, 1, None],
      '2a': ['m', 2, 0, 2, 0, 4, None, 1, None, 0, None, 0, None],
      '2b': ['m', 3, 0, 3, 0, 0, None, 0, None, 0, None, 1, None],
      '2c': ['m', 4, 0, 0, 1, 0, None, 1, None, 4, None, 1, None],
      '2d': ['m', 5, 0, 1, 1, 0, None, 2, 'door_2d_2e', 0, None, 1, None],
      '2e': ['m', 6, 0, 2, 1, 0, None, 2, 'door_2e_2f', 0, None, 0, None],
      '2f': ['m', 7, 0, 3, 1, 0, None, 0, None, 0, None, 0, None],
      '2g': ['m', 8, 1, 0, 2, 0, None, 1, None, 0, None, 0, None],
      '2h': ['m', 9, 0, 1, 2, 0, None, 0, None, 0, None, 0, None],

      '2i': ['n', 1, 0, 1, 0, 4, None, 1, None, 0, None, 1, None],
      '2j': ['n', 2, 0, 2, 0, 0, None, 1, None, 0, None, 0, None],
      '2k': ['n', 3, 0, 3, 0, 0, None, 0, None, 0, None, 1, None],
      '2l': ['n', 4, 0, 0, 1, 0, None, 1, None, 0, None, 0, None],
      '2m': ['n', 5, 0, 1, 1, 0, None, 1, None, 0, None, 0, None],
      '2n': ['n', 6, 0, 2, 1, 0, None, 1, None, 0, None, 1, None],
      '2o': ['n', 7, 0, 3, 1, 0, None, 1, None, 0, None, 0, None],
      '2p': ['n', 8, 0, 4, 1, 0, None, 0, None, 0, None, 0, None],
      '2q': ['n', 9, 1, 2, 2, 0, None, 0, None, 0, None, 0, None],

      '2r': ['t', 1, 1, 0, 0, 0, None, 1, None, 0, None, 0, None],
      '2s': ['t', 2, 0, 1, 0, 0, None, 1, None, 0, None, 0, None],
      '2t': ['t', 3, 0, 2, 0, 0, None, 1, None, 0, None, 0, None],
      '2u': ['t', 4, 0, 3, 0, 0, None, 4, None, 0, None, 0, None]
    }

    AREAS = {
      'b': [136, 104, 11, 24, ['1r', '1s', '1t', '1u', '1v', '1w', '1x', '1y']],
      'c': [184, 80, 27, 18, ['1a', '1b', '1c', '1d', '1e', '1f', '1g']],
      'm': [160, 104, 28, 26, ['1z', '2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h']],
      'n': [160, 104, 17, 26, ['2i', '2j', '2k', '2l', '2m', '2n', '2o', '2p', '2q']],
      't': [128, 32, 24, 24, ['2r', '2s', '2t', '2u']],
      'w': [92, 176, 15, 16, ['1h', '1i', '1j', '1k', '1l', '1m', '1n', '1o', '1p', '1q']]
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

    ROOM_TYPES = {
      0: 'normal',
      1: 'boss',
      2: 'secret'
    }

    ROOM_STATES = {
      'N': 'undiscovered',
      'Y': 'discovered',
      'C': 'completed'
    }

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)
        self.remove_background()
        self.add_mode_event_handler('cmd_map_position', self.event_set_location)
        self.add_mode_event_handler('cmd_map_complete', self.event_complete_location)
        self.machine.events.post('map_is_initialized')

    def mode_stop(self, **kwargs):
        super().mode_stop(**kwargs)

    def event_set_location(self, **kwargs):
        room_code = kwargs.get('room', '1b')
        area_code = self.LAYOUT[room_code][0]

        if kwargs.get('visit', False):
            player_var = 'map_visited_{}'.format(area_code)
            current_visits = list(self.player[player_var])

            if current_visits[self.LAYOUT[room_code][1] - 1] == 'N':
                current_visits[self.LAYOUT[room_code][1] - 1] = 'Y'
                self.player['rooms_visited'] = self.player['rooms_visited'] + 1

            self.player[player_var] = "".join(current_visits)

        self.player.map_location = room_code
        self.draw_map(area_code)

    def event_complete_location(self, **kwargs):
        room_code = kwargs.get('room', '1b')
        area_code = self.LAYOUT[room_code][0]

        player_var = 'map_visited_{}'.format(area_code)
        current_visits = list(self.player[player_var])

        current_visits[self.LAYOUT[room_code][1] - 1] = 'C'

        self.player[player_var] = "".join(current_visits)

        self.draw_map(area_code)

    def draw_map(self, area_code):
        self.remove_background()
        self.draw_background(area_code)

        self.remove_player()

        for room_number in range(1, 11):
            self.remove_room(room_number)
            self.remove_exit(room_number, 'n')
            self.remove_exit(room_number, 'e')
            self.remove_exit(room_number, 'w')
            self.remove_exit(room_number, 's')

        for room_code in self.AREAS[area_code][4]:
            self.draw_map_tile(room_code)

    def draw_map_tile(self, room_code):
        area_code, room_number, room_type, x, y, exit_n_type, exit_n_var, exit_e_type, exit_e_var, exit_w_type, exit_w_var, exit_s_type, exit_s_var = self.LAYOUT.get(room_code)

        x = self.ORIGIN_X - self.AREAS[area_code][0] + self.AREAS[area_code][2] + (x * 32)
        y = self.ORIGIN_Y - self.AREAS[area_code][3] - (y * 32)

        self.draw_room(room_number, x, y, room_type, list(self.player['map_visited_{}'.format(self.LAYOUT[room_code][0])])[room_number - 1])
        self.draw_exit(room_number, 'n', x, y + 14, exit_n_type, exit_n_var)
        self.draw_exit(room_number, 'e', x + 16, y, exit_e_type, exit_e_var)
        self.draw_exit(room_number, 'w', x - 14, y, exit_w_type, exit_w_var)
        self.draw_exit(room_number, 's', x, y - 16, exit_s_type, exit_s_var)

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

    def draw_room(self, room_number, x, y, room_type, room_state):
        settings = {
          'map_tile_{}'.format(room_number): {
            'action': 'add',
            'target': 'window',
            'key': 'map_room_{}'.format(room_number),
            'widget_settings': {
              'x': x,
              'y': y,
              'z': 1001,
              'image': 'map_tile_{}_{}'.format(self.ROOM_TYPES[room_type], self.ROOM_STATES[room_state])
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

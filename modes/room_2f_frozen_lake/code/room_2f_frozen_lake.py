from random import randint
from random import sample
from mpf.core.mode import Mode

class Room2fFrozenLake(Mode):

    def mode_start(self, **kwargs):
        self.add_mode_event_handler('room_2f_choose_next_shot', self.event_add_a_shot)
        self.add_mode_event_handler('room_2f_reset_shots', self.event_reset_shots)

        self.event_reset_shots(**kwargs)

        super().mode_start(**kwargs)

    def event_add_a_shot(self, **kwargs):
        player = self.machine.game.player

        if len(player['room_2f_target_order']) > 0:
            next_shot = ord(player['room_2f_target_order'][:1]) - 64
            player['room_2f_target_order'] = player['room_2f_target_order'][1:]
            self.machine.events.post('room_2f_enable_shot_{}'.format(next_shot))
        else:
            self.machine.events.post('room_2f_enable_scoop_shot')


    def event_reset_shots(self, **kwargs):
        player = self.machine.game.player
        player['room_2f_target_order'] = 'ABCDEFGHIJKLMN'
        player['room_2f_target_order'] = self.shuffle_shots(player['room_2f_target_order'][:10]) + self.shuffle_shots(player['room_2f_target_order'][10:])
        self.event_add_a_shot(**kwargs)

    def shuffle_shots(self, s):
        return ''.join(sample(s,len(s)))

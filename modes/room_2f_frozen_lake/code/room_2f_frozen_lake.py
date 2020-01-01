from random import randint
from random import shuffle
from mpf.core.mode import Mode

class Room2fFrozenLake(Mode):

    def mode_start(self, **kwargs):
        # self.player['room_2f_target_order'] = shuffle(self.player.room_2f_target_order)

        self.add_mode_event_handler('room_2f_choose_next_shot', self.event_add_a_shot)
        self.event_add_a_shot(**kwargs)

        super().mode_start(**kwargs)

    def event_add_a_shot(self, **kwargs):
        if len(player['room_2f_target_order']) > 0:
            # next_shot = ord(self.player.room_2f_target_order[0]) - 64
            # self.player['room_2f_target_order'] = self.player.room_2f_target_order[1:]
            self.machine.events.post('room_2f_enable_shot_{}'.format(randint(1, 14))

from random import randint
from random import shuffle
from mpf.core.mode import Mode

class Room2fFrozenLake(Mode):

    def mode_start(self, **kwargs):
        self.add_mode_event_handler('room_2f_choose_next_shot', self.event_add_a_shot)
        self.event_add_a_shot(**kwargs)

        player = self.machine.game.player

        # if shot sequence is 0 characters long then reset pattern to default
        if len(player['room_2f_target_order']) == 0:
            player['room_2f_target_order'] = 'ABCDEFGHIJKLMN'

        # if shot sequence is 14 characters long
        #    shuffle first 10
        #    shuffle last 4

        super().mode_start(**kwargs)

    def event_add_a_shot(self, **kwargs):
        # only if shots are left:
        #   pop off first character
        #   subtract 65 and save as next shot
        #   save abbreviated shot list
        self.machine.events.post('room_2f_enable_shot_{}'.format(randint(1, 14)))

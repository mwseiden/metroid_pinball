from random import randint
from random import sample
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
        self.warning_log("WTF %s", len(player['room_2f_target_order']))
        if len(player['room_2f_target_order']) == 14:
            player['room_2f_target_order'] = self.shuffle_shots(player['room_2f_target_order'][:10]) + self.shuffle_shots(player['room_2f_target_order'][10:])
            self.warning_log("WTF %s", player['room_2f_target_order'])

        super().mode_start(**kwargs)

    def event_add_a_shot(self, **kwargs):
        player = self.machine.game.player

        # only if shots are left:
        #   pop off first character
        #   subtract 64 and save as next shot
        #   save abbreviated shot list
        if len(player['room_2f_target_order']) > 0:
            next_shot = ord(player['room_2f_target_order'][:1]) - 64
            player['room_2f_target_order'] = player['room_2f_target_order'][1:]
            self.machine.events.post('room_2f_enable_shot_{}'.format(next_shot))

    def shuffle_shots(self, s):
        self.warning_log("WTF %s", s)
        self.warning_log("WTF %s", ''.join(sample(s,len(s))))
        return ''.join(sample(s,len(s)))

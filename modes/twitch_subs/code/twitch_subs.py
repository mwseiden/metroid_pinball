from random import randint
# from random import sample
from mpf.core.mode import Mode

class TwitchSubs(Mode):

    def mode_start(self, **kwargs):
        self.add_mode_event_handler('twitch_subscription', self.event_subscription)

        super().mode_start(**kwargs)

    def event_subscription(self, **kwargs):
        player = self.machine.game.player

        if randint(0, 1) == 0 and self.machine.game.balls_in_play == 1:
            self._teleport_player(player)
        else:
            self._reverse_flippers()

        # self.machine.game.balls_in_play
        # self.info_log('Initializing BAO Base')

    def _teleport_player(self, player):
        room_index = randint(0, 42)
        room_prefix = (room_index / 26) + 1
        room_letter = chr((room_index % 26) + ord('a'))
        self.info_log('Teleporting player to room number {}'.format(room_index))

        self.machine.events.post('twitch_subs_teleport')
        self.machine.events.post('room_{}_exit'.format(player['continue_room']))
        self.machine.events.post('room_{}{}_enter'.format(room_prefix, room_letter))

    def _reverse_flippers(self):
        self.machine.events.post('twitch_subs_reverse_flip')

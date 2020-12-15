from random import randint
from mpf.core.mode import Mode

class Room1hTeleporters(Mode):

    def mode_start(self, **kwargs):
        self.add_mode_event_handler('room_1h_teleport_shot_hit', self.event_teleport)

        super().mode_start(**kwargs)

    def event_teleport(self, **kwargs):
        room_index = randint(0, 42)
        room_prefix = int(room_index / 26) + 1
        room_letter = chr((room_index % 26) + ord('a'))
        self.info_log('Teleporting player to room number {}'.format(room_index))

        self.machine.events.post('stop_current_music')
        self.machine.events.post('room_{}_exit'.format(player['continue_room']))
        self.machine.events.post('room_{}{}_enter'.format(room_prefix, room_letter))

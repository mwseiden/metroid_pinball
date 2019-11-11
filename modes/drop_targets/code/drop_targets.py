from mpf.core.mode import Mode

class DropTargets(Mode):

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)

        self.add_mode_event_handler('drop_targets_continue', self.event_restore_drop_state)
        self.add_mode_event_handler('drop_targets_save', self.event_save_drop_state)

    def mode_stop(self, **kwargs):
        super().mode_stop(**kwargs)
        self.event_save_drop_state(**kwargs)

    def event_restore_drop_state(self, **kwargs):
        player = self.machine.game.player
        pattern = player['drops_{}'.format(player['continue_room'])] or 'UUU'

        self.machine.events.post('drop_targets_start_one' if pattern[0] == 'U' else 'cmd_drop_one_down')
        self.machine.events.post('drop_targets_start_two' if pattern[1] == 'U' else 'cmd_drop_two_down')
        self.machine.events.post('drop_targets_start_three' if pattern[2] == 'U' else 'cmd_drop_three_down')

    def event_save_drop_state(self, **kwargs):
        player = self.machine.game.player
        player['drops_{}'.format(player['continue_room'])] = self.drop_status('drop_one') + self.drop_status('drop_two') + self.drop_status('drop_three')

    def drop_status(self, name):
        return 'D' if self.machine.drop_targets[name].complete else 'U'
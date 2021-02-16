from mpf.core.mode import Mode

class Scoop(Mode):

    def mode_start(self, **kwargs):
        # self.current_music = None
        # self.current_overlay_music = None

        # self.add_mode_event_handler('cmd_play_map_music', self.event_play_map_music)
        # self.add_mode_event_handler('cmd_play_overlay_music', self.event_play_overlay_music)
        self.add_mode_event_handler('ball_hold_collect_award_shot_held_ball', self.event_ball_collected)

        super().mode_start(**kwargs)


    def event_ball_collected(self, **kwargs):
        self.machine.events.post('scoop_award_collected')


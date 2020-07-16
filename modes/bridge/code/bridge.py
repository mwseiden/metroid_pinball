from mpf.core.mode import Mode

class Bridge(Mode):

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)

        self.add_mode_event_handler('bridge_disable_autofire', self.event_disable_autofire)
        self.add_mode_event_handler('bridge_enable_autofire', self.event_enable_autofire)

        self.machine.ball_devices['bd_plunger'].config['auto_fire_on_unexpected_ball'] = True
 
    def mode_stop(self, **kwargs):
        self.machine.ball_devices['bd_plunger'].config['auto_fire_on_unexpected_ball'] = True
        super().mode_stop(**kwargs)

    def event_disable_autofire(self, **kwargs):
        self.machine.ball_devices['bd_plunger'].config['auto_fire_on_unexpected_ball'] = False

    def event_enable_autofire(self, **kwargs):
        self.machine.ball_devices['bd_plunger'].config['auto_fire_on_unexpected_ball'] = True

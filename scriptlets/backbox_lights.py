from mpf.core.scriptlet import Scriptlet
from .lights.backbox.rain import Rain

class BackBoxLights(Scriptlet):

    REFRESH_RATE = 35

    def on_load(self, **kwargs):
        set_effects_to_default()
        _schedule_update()

    def set_effects_to_default(self):
        self.base_effect = Rain(self.machine)
        self.overlay_effect = None

    def set_base_effect(self, effect):
        self.base_effect = effect

    def set_overlay_effect(self, effect):
        if self.overlay_effect == None:
            self.base_effect.save_state()

        self.overlay_effect = effect

    # private ----------------------------------------------------------------

    def _update_backbox(self, **kwargs):
        if self.overlay_effect != None:
            if self.overlay_effect.is_finished():
                self.overlay_effect = None
                self.base_effect.restore_state()
            else:
                self.overlay_effect.animate()
        elif self.base_effect != None:
            self.base_effect.animate()

        _schedule_update()

    def _schedule_update(self):
        self.delay_manager.add_if_doesnt_exist(REFRESH_RATE, self._update_backbox, 'bbup')

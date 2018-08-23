from mpf.core.scriptlet import Scriptlet
from .lights.backbox.rain import Rain
from .lights.backbox.sweep_horizontal import SweepHorizontal
from .lights.backbox.sweep_vertical import SweepVertical

class BackBoxLights(Scriptlet):

    REFRESH_RATE = 35

    def on_load(self):
        self.set_effects_to_default()
        self._schedule_update()

    def set_effects_to_default(self):
        self.base_effect = self.show_rain()
        self.overlay_effect = None

    def set_base_effect(self, effect):
        self.base_effect = effect

    def set_overlay_effect(self, effect):
        if self.overlay_effect is None:
            self.base_effect.save_state()

        self.overlay_effect = effect

    # show factories ---------------------------------------------------------

    def show_rain(self):
        return Rain(self.machine)

    def show_sweep_horizontal(self, color, speed, repeat, direction):
        return SweepHorizontal(self.machine, color, speed, repeat, direction)

    def show_sweep_vertical(self, color, speed, repeat, direction):
        return SweepVertical(self.machine, color, speed, repeat, direction)

    # private ----------------------------------------------------------------

    def _update_backbox(self, **kwargs):
        if self.overlay_effect is not None:
            if self.overlay_effect.is_finished():
                self.overlay_effect = None
                self.base_effect.restore_state()
            else:
                self.overlay_effect.animate()
        elif self.base_effect is not None:
            self.base_effect.animate()

        self._schedule_update()

    def _schedule_update(self):
        self.delay.add_if_doesnt_exist(self.REFRESH_RATE, self._update_backbox, 'bbup')

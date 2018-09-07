from mpf.core.rgb_color import RGBColor
from mpf.core.scriptlet import Scriptlet
from .lights.backbox.rain import Rain
from .lights.backbox.solid import Solid
from .lights.backbox.sweep_horizontal import SweepHorizontal
from .lights.backbox.sweep_vertical import SweepVertical

class BackBoxLights(Scriptlet):

    REFRESH_RATE = 35

    def on_load(self):
        self.set_effects_to_default()
        self._schedule_update()
        self.machine.events.add_handler('backbox_show', self._show_base_effect)
        self.machine.events.add_handler('backbox_show_overlay', self._show_overlay_effect)

    def set_effects_to_default(self):
        self.base_effect = None
        self.overlay_effect = None

    def set_base_effect(self, effect):
        self.base_effect = effect

        if effect is None:
            self._clear_lights()

    def set_overlay_effect(self, effect):
        if self.overlay_effect is None:
            self.base_effect.save_state()

        self.overlay_effect = effect

        if effect is None:
            self.base_effect.restore_state()

    # show factories ---------------------------------------------------------

    def show_rain(self, **kwargs):
        return Rain(self.machine)

    def show_solid(self, **kwargs):
        return Show(self.machine, RGBColor(kwargs.get('color', [0, 0, 0])))

    def show_sweep_horizontal(self, **kwargs):
        return SweepHorizontal(
            self.machine,
            RGBColor(kwargs.get('color', [64, 0, 0])),
            int(kwargs.get('speed', 4)),
            int(kwargs.get('repeat', 0)),
            0 if kwargs.get('direction', 'left').lower() == 'left' else 1
        )

    def show_sweep_vertical(self, **kwargs):
        return SweepVertical(
            self.machine,
            RGBColor(kwargs.get('color', [64, 0, 0])),
            int(kwargs.get('speed', 4)),
            int(kwargs.get('repeat', 0)),
            0 if kwargs.get('direction', 'left').lower() == 'left' else 1
        )

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

    def _show_base_effect(self, **kwargs):
        self.set_base_effect(self._create_show(**kwargs))

    def _show_overlay_effect(self, **kwargs):
        self.set_overlay_effect(self._create_show(**kwargs))

    def _create_show(self, **kwargs):
        shows = {
            'rain': self.show_rain,
            'solid': self.show_solid,
            'sweep_horizontal': self.show_sweep_horizontal,
            'sweep_vertical': self.show_sweep_vertical,
        }

        return shows.get(kwargs.get('show_type', 'rain').lower())(**kwargs)

    def _clear_lights(self):
        set_base_effect(show_solid(self, color='off'))

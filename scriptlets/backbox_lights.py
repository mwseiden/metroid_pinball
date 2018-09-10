from mpf.core.rgb_color import RGBColor
from mpf.core.scriptlet import Scriptlet
from .lights.backbox.cloudy_landscape import CloudyLandscape
from .lights.backbox.fire import Fire
from .lights.backbox.pour import Pour
from .lights.backbox.rain import Rain
from .lights.backbox.rain import Rainbow
from .lights.backbox.solid import Solid
from .lights.backbox.sweep_horizontal import SweepHorizontal
from .lights.backbox.sweep_vertical import SweepVertical

class BackBoxLights(Scriptlet):

    REFRESH_RATE = 35

    def on_load(self):
        self.shows = {
            'cloudy_landscape': self.show_cloudy_landscape,
            'fire': self.show_fire,
            'pour': self.show_pour,
            'rain': self.show_rain,
            'rainbow': self.show_rainbow,
            'solid': self.show_solid,
            'sweep_horizontal': self.show_sweep_horizontal,
            'sweep_vertical': self.show_sweep_vertical,
        }

        self.set_effects_to_default()
        self._schedule_update()
        self.machine.events.add_handler('cmd_backbox_show', self._show_base_effect)
        self.machine.events.add_handler('cmd_backbox_show_overlay', self._show_overlay_effect)

    def set_effects_to_default(self):
        self._clear_lights()
        self.overlay_effect = None

    def set_base_effect(self, effect):
        self.base_effect = effect

        if effect is None:
            self._clear_lights()

    def set_overlay_effect(self, effect):
        if self.overlay_effect is None and self.base_effect is not None:
            self.base_effect.save_state()

        self.overlay_effect = effect

        if effect is None and self.base_effect is not None:
            self.base_effect.restore_state()

    # show factories ---------------------------------------------------------

    def show_cloudy_landscape(self, **kwargs):
        return CloudyLandscape(self.machine)

    def show_fire(self, **kwargs):
        return Fire(self.machine)

    def show_pour(self, **kwargs):
        return Pour(
            self.machine,
            int(kwargs.get('count', 1)),
            int(kwargs.get('min_length', 5)),
            int(kwargs.get('max_length', 10)),
            RGBColor(kwargs.get('color', '400000'))
        )

    def show_rain(self, **kwargs):
        return Rain(self.machine)

    def show_rainbow(self, **kwargs):
        return Rainbow(
            self.machine,
            int(kwargs.get('speed', 4))
        )

    #def show_sunny_days_that_i_thought_would_never_end(self, **kwargs):
    #    return Sunshine(self.machine)

    def show_solid(self, **kwargs):
        return Solid(self.machine, RGBColor(kwargs.get('color', [0, 0, 0])))

    def show_sweep_horizontal(self, **kwargs):
        return SweepHorizontal(
            self.machine,
            RGBColor(kwargs.get('color', '400000')),
            int(kwargs.get('speed', 4)),
            int(kwargs.get('repeat', 0)),
            0 if kwargs.get('direction', 'left').lower() == 'left' else 1
        )

    def show_sweep_vertical(self, **kwargs):
        return SweepVertical(
            self.machine,
            RGBColor(kwargs.get('color', '400000')),
            int(kwargs.get('speed', 4)),
            int(kwargs.get('repeat', 0)),
            0 if kwargs.get('direction', 'left').lower() == 'left' else 1
        )

    # private ----------------------------------------------------------------

    def _update_backbox(self, **kwargs):
        if self.overlay_effect is not None:
            if self.overlay_effect.is_finished():
                self.overlay_effect = None
                if self.base_effect is not None:
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
        show = self.shows.get(kwargs.get('show_type', 'none').lower())
        return self._no_show() if show is None else show(**kwargs)

    def _clear_lights(self):
        self.set_base_effect(self._no_show())

    def _no_show(self):
        return self.show_solid(color='off')

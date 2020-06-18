from mpf.core.rgb_color import RGBColor
from mpf.core.scriptlet import Scriptlet
from .lights.backbox.solid_two_tone import SolidTwoTone
from .lights.backbox.fire import Fire
from .lights.backbox.pour import Pour
from .lights.backbox.drop import Drop
from .lights.backbox.rainbow import Rainbow
from .lights.backbox.solid import Solid
from .lights.backbox.sweep_horizontal import SweepHorizontal
from .lights.backbox.sweep_vertical import SweepVertical
from .lights.backbox.twinkle import Twinkle
from .lights.backbox.sparkle import Sparkle
from .lights.backbox.heat_up import HeatUp
from .lights.backbox.gradient import Gradient
from .lights.backbox.plasma import Plasma

class BackBoxLights(Scriptlet):

    REFRESH_RATE = 35

    def on_load(self):
        self.shows = {
            'two_tone': self.show_two_tone,
            'fire': self.show_fire,
            'pour': self.show_pour,
            'drop': self.show_drop,
            'rainbow': self.show_rainbow,
            'solid': self.show_solid,
            'sweep_horizontal': self.show_sweep_horizontal,
            'sweep_vertical': self.show_sweep_vertical,
            'twinkle': self.show_twinkle,
            'sparkle': self.show_sparkle,
            'heat_up': self.show_heat_up,
            'gradient': self.show_gradient,
            'plasma': self.show_plasma,
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

    def show_two_tone(self, **kwargs):
        return SolidTwoTone(
            self.machine,
            int(kwargs.get('min_cutoff', 5)),
            int(kwargs.get('max_cutoff', 5)),
            RGBColor(kwargs.get('color1', '400000')),
            RGBColor(kwargs.get('color2', '400000'))
        )

    def show_fire(self, **kwargs):
        return Fire(self.machine)

    def show_plasma(self, **kwargs):
        return Plasma(
            self.machine,
            [
                RGBColor(kwargs.get('color1', '000010')),
                RGBColor(kwargs.get('color2', '000020')),
                RGBColor(kwargs.get('color3', '000030')),
                RGBColor(kwargs.get('color4', '000040')),
                RGBColor(kwargs.get('color5', '000050')),
                RGBColor(kwargs.get('color6', '000060')),
                RGBColor(kwargs.get('color7', '000070')),
                RGBColor(kwargs.get('color8', '000080'))
            ],
            float(kwargs.get('decay_r', '1.8')),
            float(kwargs.get('decay_g', '2.6')),
            float(kwargs.get('decay_b', '3.2')),
            int(kwargs.get('repeat', None))
        )

    def show_pour(self, **kwargs):
        return Pour(
            self.machine,
            int(kwargs.get('count', 1)),
            int(kwargs.get('min_length', 5)),
            int(kwargs.get('max_length', 10)),
            RGBColor(kwargs.get('color', '400000'))
        )

    def show_drop(self, **kwargs):
        return Drop(
            self.machine,
            int(kwargs.get('min_delay', 1)),
            int(kwargs.get('max_delay', 2)),
            RGBColor(kwargs.get('background_color', '000000')),
            RGBColor(kwargs.get('drop_color', '400000'))
        )

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
            0 if kwargs.get('direction', 'down').lower() == 'down' else 1
        )

    def show_twinkle(self, **kwargs):
        return Twinkle(
            self.machine,
            RGBColor(kwargs.get('background_color', '000000')),
            RGBColor(kwargs.get('twinkle_color', '404040')),
            int(kwargs.get('twinkle_count', 4)),
            int(kwargs.get('steps', 100))
        )

    def show_sparkle(self, **kwargs):
        return Sparkle(
            self.machine,
            RGBColor(kwargs.get('background_color', '000000')),
            RGBColor(kwargs.get('color', '404040')),
            int(kwargs.get('count', 10)),
            int(kwargs.get('repeat', 0))
        )

    def show_heat_up(self, **kwargs):
        return HeatUp(
            self.machine,
            RGBColor(kwargs.get('color', 'FF0000')),
            int(kwargs.get('add_percentage', 5)),
            int(kwargs.get('steps', 20))
        )

    def show_gradient(self, **kwargs):
        return Gradient(
            self.machine,
            RGBColor(kwargs.get('color_start', '000000')),
            RGBColor(kwargs.get('color_end', '0000FF'))
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

from mpf.core.mode import Mode
from mpf.core.rgb_color import RGBColor
from ....scriptlets.lights.backbox.sweep_horizontal import SweepHorizontal

class Base(Mode):

    def mode_start(self, **kwargs):
        self.add_mode_event_handler('twitch_new_chat_message', self.chat_message)

    def chat_message(self, **kwargs):
        self._backbox_scriptlet().set_overlay_effect(SweepHorizontal(self.machine, RGBColor([128, 64, 0]), 3, 3, 0))

    # private ----------------------------------------------------------------

    def _backbox_scriptlet(self):
        for scriptlet in self.machine.scriptlets:
            if scriptlet.name == 'BackBoxLights':
                return scriptlet

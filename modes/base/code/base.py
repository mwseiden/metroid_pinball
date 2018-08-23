from mpf.core.mode import Mode
from mpf.core.rgb_color import RGBColor

class Base(Mode):

    def mode_start(self, **kwargs):
        self.add_mode_event_handler('twitch_new_chat_message', self.chat_message)
        self.add_mode_event_handler('twitch_bit_donation', self.bit_donation)

    def chat_message(self, **kwargs):
        backbox = self._backbox_scriptlet()
        backbox.set_overlay_effect(backbox.show_sweep_horizontal(RGBColor([128, 32, 0]), 1, 3, 0))

    def bit_donation(self, **kwargs):
        backbox = self._backbox_scriptlet()
        backbox.set_overlay_effect(backbox.show_sweep_horizontal(RGBColor([160, 0, 0]), 2, 9, 0))

    # private ----------------------------------------------------------------

    def _backbox_scriptlet(self):
        for scriptlet in self.machine.scriptlets:
            if scriptlet.name == 'BackBoxLights':
                return scriptlet

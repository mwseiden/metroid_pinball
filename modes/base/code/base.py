from mpf.core.mode import Mode

class Base(Mode):

    def mode_start(self, **kwargs):
        self.add_mode_event_handler('twitch_new_chat_message', self.chat_message)

    def chat_message(self, **kwargs):
        for x in self.machine.custom_code:
            self.info_log(x)

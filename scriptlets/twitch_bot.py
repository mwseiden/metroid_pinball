import os
import threading
from mpf.core.scriptlet import Scriptlet
from .twitch.twitch_client import TwitchClient

class TwitchBot(Scriptlet):
    def on_load(self):
        # Need to switch this to use machine vars and configuration
        enabled = os.environ.get('TWITCH_ENABLE')
        if enabled != None and enabled.upper() == 'TRUE':
            self.info_log('Successful connection to Twitch')
            self.client = TwitchClient(os.environ.get('TWITCH_USER'), os.environ.get('TWITCH_PASSWORD'), os.environ.get('TWITCH_CHANNEL'))
            thread = threading.Thread(target=self.client.start, args=())
            thread.daemon = True
            thread.start()

            if self.client.is_connected():
                self.info_log('Successful connection to Twitch')
            else:
                self.info_log('Connection error')


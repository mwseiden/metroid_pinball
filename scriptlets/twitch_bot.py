import os
from mpf.core.scriptlet import Scriptlet
from .twitch.twitch_client import TwitchClient

class TwitchBot(Scriptlet):
    def on_load(self):
        # Need to switch this to use machine vars and configuration
        if os.environ.get('TWITCH_ENABLE').upper() == 'TRUE':
            self.client = TwitchClient(self.machine, os.environ.get('TWITCH_USER'), os.environ.get('TWITCH_PASSWORD'), os.environ.get('TWITCH_CHANNEL'))

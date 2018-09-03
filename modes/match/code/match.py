from mpf.modes.match.code.match import Match

class MyMatch(Match):

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)

        self.add_mode_event_handler('no_match', self.no_match)
        self.add_mode_event_handler('has_match', self.has_match)

    def no_match(self, **kwargs):
        self.machine.shows['no_match_show'].play(loops=0, show_tokens=kwargs)

    def has_match(self, **kwargs):
        self.machine.shows['has_match_show'].play(loops=0, show_tokens=kwargs)


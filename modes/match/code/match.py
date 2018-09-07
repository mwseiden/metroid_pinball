from mpf.modes.match.code.match import Match

class MyMatch(Match):

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)

        self.add_mode_event_handler('no_match', self.no_match)
        self.add_mode_event_handler('has_match', self.has_match)

    def no_match(self, **kwargs):
        self.play_show('no_match_show', kwargs)

    def has_match(self, **kwargs):
        self.play_show('has_match_show', kwargs)

    def play_show(self, show_name, event_params):
        show_tokens = dict(
            match_number0=str(event_params.get('match_number0', '')),
            match_number1=str(event_params.get('match_number1', '')),
            match_number2=str(event_params.get('match_number2', '')),
            match_number3=str(event_params.get('match_number3', '')),
            winner_number=str(event_params.get('winner_number', ''))
        )
        self.machine.shows[show_name].play(loops=0, show_tokens=show_tokens)


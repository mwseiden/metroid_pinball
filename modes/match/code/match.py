from mpf.modes.match.code.match import Match

class MyMatch(Match):

    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)

        self.add_mode_event_handler('no_match', self.no_match)
        self.add_mode_event_handler('has_match', self.has_match)

    def no_match(self, **kwargs):
        show_tokens = {'match_number0': kwargs.get('match_number0', ''), 'match_number1': kwargs.get('match_number1', ''), 'match_number2': kwargs.get('match_number2', ''), 'match_number3': kwargs.get('match_number3', ''), 'winner_number': kwargs.get('winner_number', '')}
        self.machine.shows['no_match_show'].play(loops=0, show_tokens=show_tokens)

    def has_match(self, **kwargs):
        show_tokens = {'match_number0': kwargs.get('match_number0', ''), 'match_number1': kwargs.get('match_number1', ''), 'match_number2': kwargs.get('match_number2', ''), 'match_number3': kwargs.get('match_number3', ''), 'winner_number': kwargs.get('winner_number', '')}
        self.machine.shows['has_match_show'].play(loops=0, show_tokens=show_tokens)



class Player:
    def __init__(self, username):
        # used to initialize the player with a username.
        self.username = username
        self._results = []  # initializes an empty list to store results for the player

    @property
    def username(self):
        # returns the player's username
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 < len(username) < 16:
            self._username = username
        else:
            raise ValueError('Username must be a string between 2 and 16 characters, inclusive.')

    def add_result(self, result):
        # adds a result to the player's list of results.
        from result import Result  # imports here to avoid circular imports
        if isinstance(result, Result):
            self._results.append(result)
        else:
            raise TypeError('result must be an instance of Result.')

    def results(self):
        # returns a list of all results for the player.
        return self._results

    def games_played(self):
        """Returns a unique list of all games played by the player."""
        from game import Game  # imports here to avoid circular imports 
        games = {result.game for result in self._results if isinstance(result.game, Game)}  # uses a set to get unique games
        return list(games)

    def played_game(self, game):
        # returns True if the player has played the specified game; otherwise, False.
        from game import Game  # imports here to avoid circular imports
        return any(result.game == game for result in self._results if isinstance(result.game, Game))

    def num_times_played(self, game):
        # returns the number of times the player has played the specified game.
        from game import Game  # imports here to avoid circular imports
        return sum(1 for result in self._results if isinstance(result.game, Game) and result.game == game)

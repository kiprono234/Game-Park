
class Game:
    def __init__(self, title):
        self.title = title
        # initializes an empty list to store results for the game
        self._results = []  

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise ValueError('Title must be a non-empty string')

    def add_result(self, result):
        """Adds a result to the game's list of results."""
        from result import Result  # imports here  in order to avoid circular imports
        if isinstance(result, Result):
            self._results.append(result)
        else:
            raise TypeError('result must be an instance of Result.')

    def results(self):
        """Returns a list of all results for the game."""
        return self._results

    def players(self):
        """Returns a unique list of all players that played the game."""
        from player import Player  # imports here  in order to avoid circular imports
        players = {result.player for result in self._results if isinstance(result.player, Player)}  # uses a set for unique players
        return list(players)

    def average_score(self, player):
        """Returns the average score of the specified player for this game."""
        from player import Player  # imports here in order to avoid circular imports
        if not isinstance(player, Player):
            raise TypeError('player must be an instance of Player.')

        scores = [result.score for result in self._results if result.player == player]
        if not scores:
            return 0  # If there are no results, return 0 as the average

        return sum(scores) / len(scores)

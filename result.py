class Result:
    def __init__(self, player, game, score):
        from game import Game
        from player import Player

        if not isinstance(player, Player):
            raise TypeError('player is not an instance of Player')
        
        if not isinstance(game, Game):
            raise TypeError('game is not an instance of Game')
        
        self.player = player
        self.game = game
        self.score = score


        @property
        def score(self):
            return self._score
        @score.setter
        def score(self, score):
            if not isinstance(score, int) and (1< score<=5000):
                self._score = score 
            else:
                raise ValueError('score must be between 1 and 5000, inclusive.')
            
            
    
     




    
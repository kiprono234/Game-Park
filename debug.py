
from game import Game
from player import Player
from result import Result

# creates sample players
player1 = Player("game123")
player2 = Player("Kevin")

# creates sample games
game1 = Game("pool")
game2 = Game("cardi")

# creates a  sample results
result1 = Result(player1, game1, 2)
result2 = Result(player1, game2, 3)
result3 = Result(player2, game1, 1)

# adds results to players
player1.add_result(result1)
player1.add_result(result2)
player2.add_result(result3)

# adds results to games
game1.add_result(result1)
game1.add_result(result3)
game2.add_result(result2)

# debugging: prints out player results
print(f"{player1.username}'s results: {player1.results()}")
print(f"{player2.username}'s results: {player2.results()}")

# debugging: prints out all  the players for a game
print(f"Players who played {game1.title}: {game1.players()}")

# debugging: prints out  average score for a player in a game
average_score_player1_game1 = game1.average_score(player1)
print(f"{player1.username}'s average score in {game1.title}: {average_score_player1_game1}")

# debugging: Checks if player played a specific game
played = player1.played_game(game2)
print(f"Has {player1.username} played {game2.title}? {played}")

# debugging: counts the number of times a player played a specific game
num_played = player1.num_times_played(game1)
print(f"{player1.username} has played {game1.title} {num_played} times.")



      # Game Tracking System

## Overview

The Game Tracking System is a Python application designed to manage and analyze results of various games played by different players. It allows for easy tracking of players' scores, games played, and statistical analysis of their performance.

##  IT's Features

- **Player Management**: Create players with unique usernames and store their results.
- **Game Management**: Create games and associate results with them.
- **Result Tracking**: Add results for each player in a game, including scores.
- **Statistical Analysis**: Calculate average scores for players in specific games and retrieve unique lists of players and games.

## Classes

### Game

- **Attributes**:
  - `title`: The title of the game.
  - `_results`: A private list that stores results associated with the game.
  
- **Methods**:
  - `add_result(result)`: Adds a result to the game's list of results.
  - `results()`: Returns a list of all results for the game.
  - `players()`: Returns a unique list of all players that played the game.
  - `average_score(player)`: Returns the average score of a specified player for this game.

### Player

- **Attributes**:
  - `username`: The player's unique username.
  - `_results`: A private list that stores results associated with the player.

- **Methods**:
  - `add_result(result)`: Adds a result to the player's list of results.
  - `results()`: Returns a list of all results for the player.
  - `games_played()`: Returns a unique list of all games played by the player.
  - `played_game(game)`: Returns True if the player has played the specified game.
  - `num_times_played(game)`: Returns the number of times the player has played the specified game.

### Result

- **Attributes**:
  - `player`: The player associated with the result.
  - `game`: The game associated with the result.
  - `score`: The score achieved by the player in the game.

- **Methods**:
  - `score`: A property that validates the score to be an integer between 1 and 5000.

#
  Usage
Create instances of Player and Game classes:

python
Copy code
player1 = Player("game123")
game1 = Game("pool")
Create instances of the Result class to track scores:

python

result1 = Result(player1, game1, 25)
Add results to players and games:

python
player1.add_result(result1)
game1.add_result(result1)
Retrieve information:

python
print(player1.results())  # Get results for player1
print(game1.players())     # Get players who played game1
print(game1.average_score(player1))  # Get average score for player1 in game1


  # Add results to players and games
player1.add_result(result1)
player2.add_result(result2)
game1.add_result(result1)
game2.add_result(result2)

# Print results
print(player1.results())
print(game1.players())

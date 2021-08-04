import pytest
from player.player import Player

player_data = Player("Cristiano Ronaldo",7)
player_data.goal = 35
player_data.assist = 20
player_data.games = 36
player_data.red = 1
player_data.yellow = 6
player_data.ratings = 700
player_data.minutes_played = 2700

def test_player_goal_per_game_ratio():
    assert 0.972 == player_data.goal_per_game_ratio()

def test_player_goal_per_minutes_ratio():
    assert 77.14 == player_data.minutes_per_goal_ratio()


if __name__ == "__main__":
    pytest.main()
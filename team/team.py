__AUTHOR__ = "Ayodabo Tomisin"
__LICENSE__ = None
__VERSION__ = "1.0.0"

from typing import Union

class Team:

    """
    a Team class to create teams

    Attr:
        name (str): name of the team
        players (dict=None): collection of players
        game_played (int): number of games played
        points (int): number of points in a season
        wins (int): number of wins played
        loss (int): number of losses played
        draws (int): number of draws played
        goals_scored (int): number of goals scored in a season
        goals_conceded (int): number of goals conceded in a season
        goal_difference (int): number of goal difference in a season
        stadium (str): name of stadium of team
    """

    

    def __init__(self,name: str,stadium: str,players: dict=None):
        """
        Args:
            name (str): name of the team
            players (dict=None): the dictionary of players, this will have their names and other values that are associated with a player
        """
        self._name = name
        self._players = players
        self._stadium = stadium
        self._goals_scored = 0
        self._goals_conceded = 0
        self._goal_difference = 0
        self._wins = 0
        self._loss = 0
        self._draws = 0
        self._points = 0
        self._games_played = 0

    def __repr__(self):
        return f"Team<{self._name}>"

    def __str__(self):
        return self.name

    @property
    def players(self) -> dict:
        return self._players

    @players.setter
    def players(self,players: dict):
        if players is None:
            raise ValueError("You can't have a team with no players")
        self._players = players

    @property
    def name(self):
        return self._name

    @property
    def stadium(self):
        return self._stadium

    @property
    def wins(self) -> int:
        return self._wins

    @wins.setter
    def wins(self,value: int):
        if value < 0:
            raise ValueError("goals cannot be negative")
        self._wins = value

    @property
    def draws(self) -> int:
        return self._draws

    @draws.setter
    def draws(self,value: int):
        if value < 0:
            raise ValueError("draws cannot be negative")
        self._draws = value

    @property
    def loss(self) -> int:
        return self._loss

    @loss.setter
    def loss(self,value: int):
        if value < 0:
            raise ValueError("loss cannot be negative")
        self._loss = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self,value: int):
        if value < 0:
            raise ValueError("points cannot be negative")
        self._points = value

    @property
    def goals_scored(self) -> int:
        return self._wins

    @goals_scored.setter
    def goals_scored(self,value: int):
        if value < 0:
            raise ValueError("goals scored cannot be negative")
        self._goals_scored = value

    @property
    def goals_conceded(self) -> int:
        return self._goals_conceded

    @goals_conceded.setter
    def goals_conceded(self,value: int):
        if value < 0:
            raise ValueError("goals conceded cannot be negative")
        self._goals_conceded = value

    @property
    def goal_difference(self) -> int:
        return self._goal_difference

    @goal_difference.setter
    def goal_difference(self,value: int):
        self._goal_difference = value

    @property
    def games_played(self) -> int:
        return self._games_played

    @games_played.setter
    def games_played(self,value: int):
        if value < 0:
            return ValueError("games played cannot be negative")

    def calculate_goal_difference(self,goals: int, against: int):
        """calculates the goal difference for a team"""
        self.goal_difference = goals - against

    def calculate_points(self):
        """calculates the points for a team"""
        self.points = self.wins*3 + self.draws

    def add_player(self,player: str):
        """adds a player to the collection of players"""
        self.players[player] = 0

    def delete_player(self,player: str):
        """deletes a player from the collection of players if the player is already a member of the team raises error if not"""
        if player not in self.players:
            raise ValueError("The player is not a member of this team")
        del self.players[player]

    def add_players(self,players: list):
        """extends the add_player method"""
        self.players = dict(zip(players,[0 for i in range(len(players))]))

    def get_highest_scorers(self) -> Union[list,str]:
        """returns the player(s) with the highest goal scored"""
        highest = []
        max_goal = max(self.players.values())
        for player in self.players.keys():
            if self.players.get(player) == max_goal:
                highest.append(player)
        if len(highest) == 1:
            return highest[0]
        return highest

    def goals_per_game_ratio(self) -> float:
        """calculates and returns the goals per game scored by the team"""
        return self.goals_scored / self.games_played

    def points_per_game_ratio(self) -> float:
        """calculates and returns the points per game won by the team"""
        return self.points / self.games_played
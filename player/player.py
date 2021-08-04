
__AUTHOR__ = "Ayodabo Tomisin"
__LICENSE__ = None
__VERSION__ = "1.0.0"

class Player:

    """
    A class to represent a player

    Attr:
        name (str): name of player
        goal (int): number of goals scored by player
        assist (int): number of assists gotten by player
        yellow (int): number of yellow cards gotten by player
        red (int): number of red cards gotten by player
        number (int): jersey number of player
        games (int): the minutes played by the player
        minutes_played (int): number of minutes played at a certain stage in the league
    """

    def __init__(self,name: str,number: int):
        self._name = name
        self._number = number
        self._goal = 0
        self._assist = 0
        self._yellow = 0
        self._red = 0
        self._minutes_played = 0
        self._games = 0
        self._ratings = 0.0

    def __str__(self) -> str:
        return f"{self.number}. {self.name}"

    def __repr__(self) -> str:
        return f"Player<{self.number}. {self.name}"

    @property
    def name(self) -> str:
        return self._name

    @property
    def number(self):
        return self._number

    @property
    def goal(self) -> int:
        return self._goal

    @goal.setter
    def goal(self,value: int):
        if value < 0:
            raise ValueError("goals caanot be a negative number")
        self._goal = value

    @property
    def assist(self) -> int:
        return self._assist

    @assist.setter
    def assist(self,value: int):
        if value < 0:
            raise ValueError("assists won cannot be a negative number")
        self._assist = value

    @property
    def yellow(self) -> int:
        return self._yellow

    @yellow.setter
    def yellow(self,value: int):
        if value < 0:
            raise ValueError("yellows won cannot be a negative number")
        self._yellow = value

    @property
    def red(self) -> int:
        return self._red

    @red.setter
    def red(self,value: int):
        if value < 0:
            raise ValueError("reds won cannot be a negative number")
        self._red = value

    @property
    def minutes_played(self):
        return self._minutes_played

    @minutes_played.setter
    def minutes_played(self,value: int):
        if value < 0:
            raise ValueError("minutes played cannot be negative")
        self._minutes_played = value

    @property
    def games(self):
        return self._games

    @games.setter
    def games(self,value: int):
        if value < 0:
            raise ValueError("games played cannot be negative")
        self._games = value

    @property
    def ratings(self) -> float:
        return self._ratings

    @ratings.setter
    def average_rating(self,value: float):
        self._ratings = value

    def goal_per_game_ratio(self) -> float:
        """calculates and returns the goals per game ratio of the player"""
        return self.goal / self.games

    def minutes_per_goal_ratio(self) -> float:
        """calculates and returns the minutes per goal ratio of the player"""
        return self.minutes_played / self.goal

    def calculate_average_rating(self) -> float:
        """calculates and returns the ratings per game for the player"""
        return self.ratings / self.games
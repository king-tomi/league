from fixture.fixture import Fixture
from player.player import Player
from team.team import Team
from pandas import DataFrame
import random


__AUTHOR__ = "Ayodabo Tomisin"
__LICENSE__ = None
__VERSION__ = "1.0.0"


class League:

    """
    A class to represent a League season

    Attr:
        name (str): name of the league
        season (str): current season of the league 
        teams (list): list of teams in the current season
        table (pandas DataFrame): the league table
        stadiums (dict): collection of stadiums keys: names of teams, values: names of stadiums
    """

    COLUMNS = [
        "TEAM",
        "PLD",
        "W",
        "L",
        "D",
        "GF",
        "GA",
        "GD",
        "PTS"
    ]

    def __init__(self,name: str,season: str):
        self._name = name
        self._season = season
        self.table =  DataFrame()
        self._teams = []
        self._stadiums = {}

    def __str__(self):
        return f"{self.name} {self.season} season"

    def __repr__(self):
        return f"League<{self.name} {self.season} season>"

    @property
    def name(self) -> str:
        return self._name

    @property
    def season(self) -> str:
        return self._season

    @property
    def teams(self) -> list:
        return self._teams

    @teams.setter
    def teams(self,value: list):
        self._teams = value

    @property
    def stadiums(self) -> dict:
        return self._stadiums

    @stadiums.setter
    def stadiums(self,value: dict):
        self._stadiums = value

    def create_new_table(self,teams: list) -> DataFrame:
        """
        creates an empty league table from a list of teams given
        
        param: teams -> a list containing the teams
        """
        if not 16 <= len(teams) <= 20:
            raise ValueError("number of teams should be exactly between sixteen(16) and twenty(20)")
        self.teams = teams
        self.table.columns = League.COLUMNS
        self.table.index = range(1,len(teams)+1)
        self.table["TEAM"] = sorted(teams)
        for column in League.COLUMNS:
            if column == "TEAM":
                continue
            else:
                self.table[column] = [0 for _ in range(len(teams))]
        return self.table

    def get_stadiums(self,stadiums: dict):
        """
        collects and store the available stadiums for the teams
        
        param : stadium -> a dictionary containing the teams and their stadiums
        """
        if len(stadiums) != len(self.teams):
            raise ValueError("the numbers of stadiums and clubs do not match")
        self.stadiums = stadiums

    def create_fixtures(self,date :str) -> dict:
        """
        creates fixtures for each gameweek
        
        param: date -> a string containing the date of the event

        returns: a dictionary containing the fixtures generated
        """
        fixtures = {}
        mid = len(self.teams) // 2
        homes = random.sample(self.teams,mid)
        aways = []
        for team in self.teams:
            if team not in homes:
                aways.append(team)
        for index,team in enumerate(homes):
            fixtures[team] = Fixture(team,aways[index],date,self.stadiums[team])
        return fixtures

    def sort_tables_and_return(self):
        """sorts the table by points and returns it"""
        return self.table.sort_values(by=self.table["PTS"],axis=0,inplace=True)
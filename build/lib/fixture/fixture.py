import datetime

__AUTHOR__ = "Ayodabo Tomisin"
__LICENSE__ = None
__VERSION__ = "1.0.0"

class Fixture:
    """
    A class to represent a fixture between two teams

    Attr:
        home_team (str): the name of the home team
        away_team (str): the name of the away team
        date (str): the date of the fixtures
        stadium (str): the venue for the match
        time (str): the time of fixture, defaulted to None
        state (str): the state of the fixture, defaulted to not played
    """

    STATE = [
        "NOT PLAYED",
        "PLAYED",
        "CANCELLED"
    ]

    def __init__(self,home_team: str,
                 away_team: str,
                 date: str,
                 stadium: str,
                 time: str=None,
                 state: str="NOT PLAYED"
                 ):
        if self._check_date_format(date) and state in Fixture.STATE:
            date = date.strip().split("-")
            time = time.strip().split(":")
            self._home_team = home_team
            self._away_team = away_team
            self._stadium = stadium
            self._date = datetime.date(int(date[0]),int(date[1]),int(date[2]))
            self._time = datetime.time(int(time[0]),int(time[1]),0)
            self._state = state
        else:
            raise ValueError("Unaccepted date and time format passed")

    def __str__(self) -> str:
        return f"{self.date} \n{self.home_team} vs {self.away_team} \n{self.stadium} {self.time}"

    def __repr__(self) -> str:
        return f"Fixture<{self.date} \n{self.home_team} vs {self.away_team} \n{self.stadium} {self.time}>"

    @property
    def home_team(self) -> str:
        return self._home_team

    @property
    def away_team(self) -> str:
        return self._away_team

    @property
    def date(self):
        return self._date

    @property
    def stadium(self) -> str:
        return self._stadium

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self,time: str):
        self._time = time

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self,state: str):
        if state not in Fixture.STATE:
            raise ValueError("not a valid state for a fixture")
        self._state = state

    @staticmethod
    def _check_date_format(date: str) -> bool:
        """
        A private method that checks if a date falls under a certain acceptable format.
        
        format accepted:
                dd-mm-yy
            dd: day within the range 01-31
            mm: month withn the range 01-12
            yy: year starting from any number
        """
        date_list = date.strip().split("-")
        if 1 <= int(date_list[0]) <= 31 and 1 <= int(date[1]) <= 12 and len(date_list) != 3:
            return True
        return False  
from Transaction import Transaction
from Day import Day
from Month import Month
from Year import Year
from datetime import datetime

class DayOfTheWeek:
    def __init__(self, name):
        self.name = name
        self.members = []
    
    def add_member(self, trnsctn):
        if not isinstance(trnsctn, Transaction):
            raise ValueError("Error while adding Transaction to a Day of the Week...")
        self.members.append(trnsctn)


class DaysOfTheWeek:
    def __init__(self):
        self.weekdays = [DayOfTheWeek('Monday'), DayOfTheWeek('Tuesday'), DayOfTheWeek('Wednesday'), DayOfTheWeek('Thurstday'), 
                            DayOfTheWeek('Friday'), DayOfTheWeek('Saturday'), DayOfTheWeek('Sunday')]

    def which_dotw(self, trnsctn):
        if not isinstance(trnsctn, Transaction):
            raise ValueError("Error while adding Transaction to weekdays...")
        self.weekdays[datetime(year=trnsctn.year, month=trnsctn.month, day=trnsctn.day).weekday()].add_member(trnsctn)
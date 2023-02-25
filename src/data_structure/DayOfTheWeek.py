import json
from datetime import datetime
from data_structure.Transaction import Transaction
from data_structure.std_classes import StdClass

# vielleicht benötigt, dann aber anders importieren
# from Day import Day
# from Month import Month
# from Year import Year

class DayOfTheWeek(StdClass):
    def __init__(self, name: str, dayoftheweek:int):
        if dayoftheweek<1 or dayoftheweek>7:
            raise ValueError("Invalid Day of the Week...")
        super().__init__(name)
        self.dayoftheweek = dayoftheweek
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\\Time\DayOfTheWeek\\" + self.name + ".json"
        self.save()
        DaysOfTheWeek.add_member(self)
    
    def add_member(self, trnsctn):
        if not isinstance(trnsctn, Transaction):
            raise ValueError("Error while adding Transaction to a Days...")
        super().add_member(trnsctn)

    def load(self):
        all_members = super().load()
        all_members_temp = []
        for member in all_members:
            temp = Transaction(member['name'], member['value'], member['day'], member['month'], member['year'])
            all_members_temp.append(temp)
        self.members = all_members_temp


class AllDaysOfTheWeek:
    def __init__(self,):
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\Time\DaysOfTheWeek.json"
        self.members = []
        self.flag = False

    def add_member(self, dayoftheweek):
        if not isinstance(dayoftheweek, DayOfTheWeek):
            raise ValueError("Invalid Day of the week...")
        self.members.append(dayoftheweek)
        if self.flag: 
            self.save()
    
    def load(self):
        with open(self.filepath, "r") as file:
            self.__dict__ = json.load(file)
            self.flag = False
            all_names = tuple(self.members)
            for member in all_names:
                temp = DayOfTheWeek(name=member[0], dayoftheweek=member[1])
                temp.load()
                self.members.remove(member)
            file.close()
        self.flag = True

    def save(self):
        all_names = [(member.name, member.dayoftheweek) for member in self.members]
        temp_dict = self.__dict__.copy()
        temp_dict['members'] = all_names
        with open(self.filepath, "w+") as file:
            json.dump(temp_dict, file)
            file.close()

    
DaysOfTheWeek = AllDaysOfTheWeek()
DaysOfTheWeek.load()

# DaysOfTheWeek.flag = True
# liste = ["Monday", "Tuesday", "Wednesday", "Thurstday", 
#         "Friday", "Saturday", "Sunday"]
# for count, value in enumerate(liste):
#     DayOfTheWeek(name=value, dayoftheweek=count+1)

def which_day_of_the_week(year, month, day):
    return datetime(year=year, month=month, day=day).weekday()+1

def add_to_day_of_the_week(trnsctn):
    if not isinstance(trnsctn, Transaction):
        raise ValueError("Error while adding Transaction to a Days...")
    dayoftheweek = which_day_of_the_week(year=trnsctn.year, month=trnsctn.month, day=trnsctn.day)
    for member in DaysOfTheWeek.members:
        if member.dayoftheweek == dayoftheweek:
            member.add_member(trnsctn)
            break

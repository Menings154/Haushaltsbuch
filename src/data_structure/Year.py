import json
from data_structure.Transaction import Transaction
from data_structure.std_classes import StdClass


class Year(StdClass):
    def __init__(self, name: str, year:int):
        if year<1001 or year>10001:
            raise ValueError("Invalid Year...")
        super().__init__(name)
        self.year = year
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\\Time\Years\\" + self.name + ".json"
        self.save()
        Years.add_member(self)
    
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


class AllYears:
    def __init__(self,):
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\Time\Years.json"
        self.members = []
        self.flag = False

    def add_member(self, year):
        if not isinstance(year, Year):
            raise ValueError("Invalid Year...")
        self.members.append(year)
        if self.flag: 
            self.save()
    
    def load(self):
        with open(self.filepath, "r") as file:
            self.__dict__ = json.load(file)
            self.flag = False
            all_names = tuple(self.members)
            for member in all_names:
                temp = Year(name=member[0], year=member[1])
                temp.load()
                self.members.remove(member)
            file.close()
        self.flag = True

    def save(self):
        all_names = [(member.name, member.year) for member in self.members]
        temp_dict = self.__dict__.copy()
        temp_dict['members'] = all_names
        with open(self.filepath, "w+") as file:
            json.dump(temp_dict, file)
            file.close()

Years = AllYears()
Years.load()
# Years.load()
# Days.flag = True

# for i in range(1, 32):
#     Day(name=str(i), day=i)

# [print(member.name, member.day) for member in Days.members]
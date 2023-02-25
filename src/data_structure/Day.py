import json
from data_structure.Transaction import Transaction
from data_structure.std_classes import StdClass


class Day(StdClass):
    def __init__(self, name, day:int):
        if day < 1 or day > 31:
            raise ValueError("Invalid Day...")
        super().__init__(name)
        self.day = day
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\\Time\Days\\" + self.name + ".json"
        self.save()
        Days.add_member(self)
    
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


class AllDays:
    def __init__(self,):
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\Time\Days.json"
        self.members = []
        self.flag = False

    def add_member(self, day):
        if not isinstance(day, Day):
            raise ValueError("Invalid Day...")
        self.members.append(day)
        if self.flag: 
            self.save()
    
    def load(self):
        with open(self.filepath, "r") as file:
            self.__dict__ = json.load(file)
            self.flag = False
            all_names = tuple(self.members)
            for member in all_names:
                temp = Day(name=member[0], day=member[1])
                temp.load()
                self.members.remove(member)
            file.close()
        self.flag = True

    def save(self):
        all_names = [(member.name, member.day) for member in self.members]
        temp_dict = self.__dict__.copy()
        temp_dict['members'] = all_names
        with open(self.filepath, "w+") as file:
            json.dump(temp_dict, file)
            file.close()

Days = AllDays()
Days.load()
# Days.flag = True

# for i in range(1, 32):
#     Day(name=str(i), day=i)

# [print(member.name, member.day) for member in Days.members]
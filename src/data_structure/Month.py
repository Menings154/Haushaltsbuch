import json
from data_structure.Transaction import Transaction
from data_structure.std_classes import StdClass


class Month(StdClass):
    def __init__(self, name, month:int):
        if month < 1 or month > 12:
            raise ValueError("Invalid Month...")
        super().__init__(name)
        self.month = month
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\\Time\Months\\" + self.name + ".json"
        self.save()
        Months.add_member(self)
    
    def add_member(self, trnsctn):
        if not isinstance(trnsctn, Transaction):
            raise ValueError("Error while adding Transaction to a Month...")
        super().add_member(trnsctn)

    def load(self):
        all_members = super().load()
        all_members_temp = []
        for member in all_members:
            temp = Transaction(member['name'], member['value'], member['day'], member['month'], member['year'])
            all_members_temp.append(temp)
        self.members = all_members_temp


class AllMonths:
    def __init__(self,):
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\Time\Months.json"
        self.members = []
        self.flag = False

    def add_member(self, month):
        if not isinstance(month, Month):
            raise ValueError("Invalid Month...")
        self.members.append(month)
        if self.flag: 
            self.save()
    
    def load(self):
        with open(self.filepath, "r") as file:
            self.__dict__ = json.load(file)
            self.flag = False
            all_names = tuple(self.members)
            for member in all_names:
                temp = Month(name=member[0], month=member[1])
                temp.load()
                self.members.remove(member)
            file.close()
        self.flag = True

    def save(self):
        all_names = [(member.name, member.month) for member in self.members]
        temp_dict = self.__dict__.copy()
        temp_dict['members'] = all_names
        with open(self.filepath, "w+") as file:
            json.dump(temp_dict, file)
            file.close()

Months = AllMonths()
Months.load()
# Months.flag = True
# #Months.load()
# month_names = ["January", "February", "March", "April", "May", "June",
#                "July","August", "Sebtember", "Oktober", "November", "December"]
# for count, value in enumerate(month_names):
#     Month(name=value, month=count+1)
# [print(member.name, member.month) for member in Months.members]
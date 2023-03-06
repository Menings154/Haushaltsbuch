import json
from data_structure.Transaction import Transaction
from data_structure.std_classes import StdClass

class SpecificMonth(StdClass):
    def __init__(self, name, month:int, year:int):
        if month < 1 or month > 12:
            raise ValueError("Invalid Month...")
        if year<1001 or year>10001:
            raise ValueError("Invalid Year...")
        super().__init__(name)
        self.month = month
        self.year = year
        self.start_balance = None
        self.final_balance = None
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\\Time\SpecificMonths\\" + self.name + ".json"
        #self.save()
        SpecificMonths.add_member(self)
    
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

    def add_start_balance(self, value):
        self.start_balance = value
    
    def add_final_balance(self, value):
        self.final_balance = value

class AllSpecificMonths:
    def __init__(self,):
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\Time\SpecificMonths.json"
        self.members = []
        self.flag = False

    def add_member(self, specificmonth):
        if not isinstance(specificmonth, SpecificMonth):
            raise ValueError("Invalid Specific month...")
        self.members.append(specificmonth)
        if self.flag:
            self.save()
    
    def load(self):
        with open(self.filepath, "r") as file:
            self.__dict__ = json.load(file)
            self.flag = False
            all_names = tuple(self.members)
            for member in all_names:
                temp = SpecificMonth(name=member[0], month=member[1], year=member[2])
                temp.load()
                self.members.remove(member)
            file.close()
        self.flag = True

    def save(self):
        all_names = [(member.name, member.month, member.year) for member in self.members]
        temp_dict = self.__dict__.copy()
        temp_dict['members'] = all_names
        with open(self.filepath, "w+") as file:
            json.dump(temp_dict, file)
            file.close()

SpecificMonths = AllSpecificMonths()
SpecificMonths.load()
# # Months.load()
# SpecificMonths.flag = True
# SpecificMonth(name="January2022", month=1, year=2022)
# #Months.load()
# month_names = ["January", "February", "March", "April", "May", "June",
#                "July","August", "Sebtember", "Oktober", "November", "December"]
# for count, value in enumerate(month_names):
#     Month(name=value, month=count+1)
# [print(member.name, member.month) for member in Months.members]
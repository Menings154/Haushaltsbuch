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
    def __init__(self):
        self.members = []

    def add_member(self, month):
        if not isinstance(month, Month):
            raise ValueError("Invalid Month...")
        self.members.append(month)

    def load(self):
        pass

    def save(self):
        pass


Months = AllMonths()
for i in range(1, 13):
    Months.add_member(i)
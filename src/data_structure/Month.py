from Transaction import Transaction

class Month:
    def __init__(self, month:int):
        if month < 1 or month > 12:
            raise ValueError("Invalid Month...")
        self.month = month
        self.members = []
    
    def add_member(self, trnsctn):
        if not isinstance(trnsctn, Transaction):
            raise ValueError("Error while adding Transaction to a Month...")
        self.members.append(trnsctn)


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
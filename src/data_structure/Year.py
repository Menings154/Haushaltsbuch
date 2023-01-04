from Transaction import Transaction

class Year:
    def __init__(self, year:int):
        if type(year) != int :
            raise ValueError("Invalid Year...")
        self.year = year
        self.members = []
    
    def add_members(self, trnsctn):
        if not isinstance(trnsctn, Transaction):
            raise ValueError("Error while adding Transaction to a Year...")
        self.members.append(trnsctn)
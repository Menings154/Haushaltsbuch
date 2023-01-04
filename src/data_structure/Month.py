from Transaction import Transaction

class Month:
    def __init__(self, month:int):
        if month < 1 or month > 12:
            raise ValueError("Invalid Month...")
        self.month = month
        self.members = []
    
    def add_members(self, trnsctn):
        if not isinstance(trnsctn, Transaction):
            raise ValueError("Error while adding Transaction to a Month...")
        self.members.append(trnsctn)

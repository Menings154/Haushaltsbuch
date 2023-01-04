from Transaction import Transaction

class Day:
    def __init__(self, day:int):
        if day < 1 or day >31:
            raise ValueError("Invalid Day...")
        self.day = day
        self.members = []

    def add_members(self, trnsctn):
        if not isinstance(trnsctn, Transaction):
            raise ValueError("Error while adding Transaction to a Day...")
        self.members.append(trnsctn)
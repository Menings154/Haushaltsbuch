from Transaction import Transaction

class Category:
    def __init__(self, name):
        self.name = name
        self.members = []
    
    def add_member(self, trnsctn):
        if not isinstance(trnsctn, Transaction):
            raise ValueError("Error while adding Transaction to a category...")
        self.members.append(trnsctn)
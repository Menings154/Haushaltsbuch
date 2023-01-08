from data_structure.Transaction import Transaction
#from Categorizer import CategorizerInstance

class Category:
    def __init__(self, name):
        self.name = name
        Categories.add_member(self)
        self.members = []
    
    def add_member(self, trnsctn):
        if not isinstance(trnsctn, Transaction):
            raise ValueError("Error while adding Transaction to a category...")
        self.members.append(trnsctn)


"all categories erstellen"
class AllCategories:
    def __init__(self,):
        self.members = []
        self.load()    

    def add_member(self, category):
        if not isinstance(category, Category):
            raise ValueError("Invalid Category...")
        self.members.append(category)
    
    def load(self):
        pass

    def save(self):
        pass


Categories = AllCategories()
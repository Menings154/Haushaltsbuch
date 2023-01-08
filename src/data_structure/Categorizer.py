# from Transaction import Transaction
from data_structure.Category import Category, Categories


class Categorizer:
    def __init__(self):
        self.lut = {} # später loading from file oder so adden struktur dic[trnctn.name] = category
        self.input_txt = "This Transaction has yet not been categorized. \n Please add or map a category to this transaction. \n Following the exsisting category: "
        # self.categories = None
    
    def load(self): # lut
        pass

    def save(self):
        pass

    def add_lut(self, trnsctn, category):
        # if not isinstance(trnsctn, Transaction):
        #     raise ValueError("Invalid transaction...")
        # if not isinstance(category, Category):
        #     raise ValueError("invalid category...")    
        self.lut[trnsctn.name] = category
    
    def categorize(self, trnsctn):
        # if not isinstance(trnsctn, Transaction):
        #    raise ValueError("Invalid transaction...")
        try:
            return self.lut[trnsctn.name]
        except:
            self.new_relation(trnsctn)
    
    def new_relation(self, trnsctn):
        # if not isinstance(trnsctn, Transaction):
        #     raise ValueError("Invalid transaction...")
        self.change_input_txt()
        new_trns_cat_relation = input(self.input_txt)
        for category in Categories.members:
            if new_trns_cat_relation == category.name:
                return category
        return Category(new_trns_cat_relation)

    def change_input_txt(self):
        for category in Categories.members:
            self.input_txt += "\n" 
            self.input_txt += category 


CategorizerInstance = Categorizer()
CategorizerInstance.load()
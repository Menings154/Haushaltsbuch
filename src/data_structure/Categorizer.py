# from Transaction import Transaction
from data_structure.Category import Category, Categories
from data_structure.Saver import Saver

class Categorizer(Saver):
    def __init__(self):
        self.filepath = r".\data\saved objects\Categorizer.json"
        self.lut = {} # später loading from file oder so adden struktur dic[trnctn.name] = category
        self.input_txt = "This Transaction has not been categorized yet. \n Please add or map a category to this transaction. \n Following the exsisting category: "
        # self.categories = None

    def add_lut(self, trnsctn, category):
        # if not isinstance(trnsctn, Transaction):
        #     raise ValueError("Invalid transaction...")
        # if not isinstance(category, Category):
        #     raise ValueError("invalid category...")    
        self.lut[trnsctn.name] = category
        self.save()
    
    def categorize(self, trnsctn):
        # if not isinstance(trnsctn, Transaction):
        #    raise ValueError("Invalid transaction...")
        try:
            return self.lut[trnsctn.name]
        except:
            return self.new_relation(trnsctn)
    
    def new_relation(self, trnsctn):
        # if not isinstance(trnsctn, Transaction):
        #     raise ValueError("Invalid transaction...")
        self.change_input_txt()
        new_trns_cat_relation = input(self.input_txt)
        for category in Categories.members:
            if new_trns_cat_relation == category.name:
                self.add_lut(trnsctn, category)
                return category
        category = Category(new_trns_cat_relation)
        self.add_lut(trnsctn, category)
        return category

    def change_input_txt(self):
        for category in Categories.members:
            self.input_txt += "\n" 
            self.input_txt += category 


CategorizerInstance = Categorizer()
#CategorizerInstance.load()
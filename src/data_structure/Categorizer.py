# from Transaction import Transaction
from data_structure.Category import Category, Categories
# from data_structure.Saver import Saver, CollectionSaver
import json

class Categorizer:
    def __init__(self):
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\Categorizer.json"
        self.lut = {} # später loading from file oder so adden struktur dic[trnctn.name] = category
        self.input_txt = "This Transaction has not been categorized yet. \n Please add or map a category to this transaction. \n Following the exsisting categories:\n"
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
            self.input_txt += ' > '
            self.input_txt += category.name
            self.input_txt += "\n" 
            
    def load(self):
        with open(self.filepath ,"r") as file:
            temp = json.load(file)
            file.close()
        for key in temp.keys():
            for category in Categories.members:
                if category.name == temp[key]:
                    self.lut[key] = category
                    break

    def save(self):
        temp_dict = {}
        for key in self.lut.keys():
            temp_dict[key] = self.lut[key].name
        with open (self.filepath, "w") as file:
            json.dump(temp_dict, file)
            file.close()


CategorizerInstance = Categorizer()
CategorizerInstance.load()
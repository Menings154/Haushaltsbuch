import json
from data_structure.Transaction import Transaction
from data_structure.Saver import Saver
#from Categorizer import CategorizerInstance

class Category(Saver):
    def __init__(self, name):
        self.name = name
        try:
            Categories.add_member(self)
        except AttributeError:
            pass
        self.members = []
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\Categories\\" + self.name + ".json"
        self.save()

    def add_member(self, trnsctn):
        if not isinstance(trnsctn, Transaction):
            raise ValueError("Error while adding Transaction to a category...")
        self.members.append(trnsctn)
        self.save()
    
    def save(self):
        trns_temp = [trns.__dict__ for trns in self.members]
        temp_dict = self.__dict__
        temp_dict["members"] = trns_temp
        with open(self.filepath, "w+") as file:
            json.dump(temp_dict, file)
            file.close()

    def load(self):
        with open(self.filepath, "r") as file:
            self.__dict__ = json.load(file)
            all_members = self.members
            all_members_temp = []
            for member in all_members:
                temp = Transaction(member['name'], member['value'], member['day'], member['month'], member['year'])
                all_members_temp.append(temp)
            self.members = all_members_temp
            file.close()

class AllCategories:
    def __init__(self,):
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\AllCategories.json"
        self.members = []

    def add_member(self, category):
        if not isinstance(category, Category):
            raise ValueError("Invalid Category...")
        self.members.append(category)
        self.save()
    
    def load(self):
        with open(self.filepath, "r") as file:
            self.__dict__ = json.load(file)
            all_names = tuple(self.members)
            for member in all_names:
                temp = Category(name=member)
                temp.load()
                self.members.remove(member)
                #all_members_temp.append(temp)
            #self.members = all_members_temp
            file.close()

    def save(self):
        all_names = [member.name for member in self.members]
        temp_dict = self.__dict__
        temp_dict['members'] = all_names
        with open(self.filepath, "w+") as file:
            json.dump(temp_dict, file)
            file.close()


Categories = AllCategories()
Categories.load()
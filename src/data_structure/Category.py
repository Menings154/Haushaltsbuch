import json
from data_structure.Transaction import Transaction
from data_structure.std_classes import StdClass

class Category(StdClass):
    def __init__(self, name):
        super().__init__(name)
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\Categories\\" + self.name + ".json"
#        self.save()
        Categories.add_member(self)
    
    def add_member(self, trns):
        if not isinstance(trns, Transaction):
            raise ValueError("Error while adding Transaction to a category...")
        super().add_member(trns)
        #self.save()
    
    def load(self):
        all_members = super().load()
        all_members_temp = []
        for member in all_members:
            temp = Transaction(member['name'], member['value'], member['day'], member['month'], member['year'])
            all_members_temp.append(temp)
        self.members = all_members_temp


class AllCategories:
    def __init__(self,):
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\AllCategories.json"
        self.members = []
        self.flag = False

    def add_member(self, category):
        if not isinstance(category, Category):
            raise ValueError("Invalid Category...")
        self.members.append(category)
        if self.flag: 
            self.save()
    
    def load(self):
        with open(self.filepath, "r") as file:
            self.__dict__ = json.load(file)
            self.flag = False
            all_names = tuple(self.members)
            for member in all_names:
                temp = Category(name=member)
                temp.load()
                self.members.remove(member)
            file.close()
        self.flag = True

    def save(self):
        all_names = [member.name for member in self.members]
        temp_dict = self.__dict__.copy()
        temp_dict['members'] = all_names
        with open(self.filepath, "w+") as file:
            json.dump(temp_dict, file)
            file.close()


Categories = AllCategories()
Categories.load()

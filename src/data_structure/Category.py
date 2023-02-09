import json
from data_structure.Transaction import Transaction
# from data_structure.Saver import Saver
#from Categorizer import CategorizerInstance
from data_structure.std_classes import StdClass

# class Category(Saver):
#     def __init__(self, name):
#         self.name = name
#         try:
#             Categories.add_member(self)
#         except AttributeError:
#             pass
#         self.members = []
#         self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\Categories\\" + self.name + ".json"
#         self.save()

#     def add_member(self, trnsctn):
#         if not isinstance(trnsctn, Transaction):
#             raise ValueError("Error while adding Transaction to a category...")
#         self.members.append(trnsctn)
#         self.save()
    
#     def save(self):
#         trns_temp = [trns.__dict__ for trns in self.members]
#         temp_dict = self.__dict__
#         temp_dict["members"] = trns_temp
#         with open(self.filepath, "w+") as file:
#             json.dump(temp_dict, file)
#             file.close()

#     def load(self):
#         with open(self.filepath, "r") as file:
#             self.__dict__ = json.load(file)
#             all_members = self.members
#             all_members_temp = []
#             for member in all_members:
#                 temp = Transaction(member['name'], member['value'], member['day'], member['month'], member['year'])
#                 all_members_temp.append(temp)
#             self.members = all_members_temp
#             file.close()

# new category test

class Category(StdClass):
    def __init__(self, name):
        # try: # wahrscheinlich ist hier das Problem
        # except AttributeError:
        #     pass
        super().__init__(name)
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\Categories\\" + self.name + ".json"
        self.save()
        Categories.add_member(self)
    
    def add_member(self, trns):
        if not isinstance(trns, Transaction):
            raise ValueError("Error while adding Transaction to a category...")
        super().add_member(trns)
    
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
        self.flag = False # warum klappt das hier nicht?

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
                #all_members_temp.append(temp)
            #self.members = all_members_temp
            file.close()
        self.flag = True

    def save(self):
        all_names = [member.name for member in self.members]
        temp_dict = self.__dict__
        temp_dict['members'] = all_names
        with open(self.filepath, "w+") as file:
            json.dump(temp_dict, file)
            file.close()

# class AllCategories(StdClass):
#     def __init__(self,):
#         super().__init__("Categories")
#         self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\AllCategories.json"


#     def add_member(self, category):
#         if not isinstance(category, Category):
#             raise ValueError("Invalid Category...")
#         super().add_member()
    
#     def load(self):
#         all_members = super().load()
#         all_names = all_members
#         with open(self.filepath, "r") as file:
#             self.__dict__ = json.load(file)
#             all_names = tuple(self.members)
#             for member in all_names:
#                 temp = Category(name=member)
#                 temp.load()
#                 self.members.remove(member)
#                 #all_members_temp.append(temp)
#             #self.members = all_members_temp
#             file.close()

#     def save(self):
#         all_names = [member.name for member in self.members]
#         temp_dict = self.__dict__
#         temp_dict['members'] = all_names
#         with open(self.filepath, "w+") as file:
#             json.dump(temp_dict, file)
#             file.close()


Categories = AllCategories()
Categories.load()





# muss getestet werden
# from Category import Category
import json
from data_structure.Saver import Saver, CollectionSaver

class Transaction(Saver):
    def __init__(self, name, value, day, month, year):
        self.name = name
        self.value = value
        self.day = day
        self.month = month
        self.year = year
        self.category = None
        self.filepath = r".\data\saved objects\Transactions\\" + str(name) + str(day) + str(month) + str(year) +".json"
        # ist diese Datenstruktur so gut gelöst?
        self.save()
        Transactions.add_member(self)
        
    def add_category(self, category): # macht das hier so sinn?
        # if not isinstance(category, Category):
        #     raise ValueError("Invalid category...")
        self.category = category
        self.save


class AllTransactions(CollectionSaver):
    def __init__(self):
        self.filepath = r".\data\saved objects\AllTransitions.json"
        self.members = []
        self.Object = Transaction

    def add_member(self, trns):
        if not isinstance(trns, Transaction):
            raise ValueError("Invalid Transaction...")
        self.members.append(trns)
        self.save()

    # def save(self):
    #     trns_temp = [trns.__dict__ for trns in self.members]
    #     temp_dict = self.__dict__
    #     temp_dict["members"] = trns_temp
    #     with open(self.filepath, "w+") as file:
    #         json.dump(temp_dict, file)
    #         file.close()

    # def load(self):
    #     file = open(self.filepath, "r")
    #     self.__dict__ = json.load(file)
    #     all_members = self.members
    #     all_members_temp = []
    #     for member in all_members:
    #         temp = Transaction(member['name'], member['value'], member['day'], member['month'], member['year'])
    #         all_members_temp.append(temp)
    #     self.members = all_members_temp


Transactions = AllTransactions()
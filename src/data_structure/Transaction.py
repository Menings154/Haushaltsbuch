# from Category import Category
import json

class Transaction:
    def __init__(self, name, value, day, month, year):
        self.name = name
        self.value = value
        self.day = day
        self.month = month
        self.year = year
        self.category = None
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\Transactions\\" + str(name) + str(day) + str(month) + str(year) +".json"
        # ist diese Datenstruktur so gut gelöst?
        self.save()
        Transactions.add_member(self)
        
    def add_category(self, category): # macht das hier so sinn?
        # if not isinstance(category, Category):
        #     raise ValueError("Invalid category...")
        self.category = category
        self.save

    def load(self):
        with open(self.filepath, "r") as file:
            self.__dict__ = json.load(file)
            file.close()

    def save(self):
        with open(self.filepath, "w+") as file:
            json.dump(self.__dict__, file)
            file.close()


class AllTransactions:
    def __init__(self):
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\AllTransitions.json"
        self.members = []

    def add_member(self, trns):
        if not isinstance(trns, Transaction):
            raise ValueError("Invalid Transaction...")
        self.members.append(trns)
        self.save()

    def load(self):
        with open(self.filepath, "r") as file:
            self.__dict__ = json.load(file)
            all_members = self.members
            all_members_temp = []
            for member in all_members:
                    temp = Transaction(member['name'], member['value'],
                                        member['day'], member['month'],
                                        member['year'])
            all_members_temp.append(temp)
            self.members = all_members_temp
            file.close()
        
    def save(self):
        object_temp = [trns.__dict__ for trns in self.members]
        temp_dict = self.__dict__.copy()
        temp_dict["members"] = object_temp
        for member in temp_dict["members"]:
            if member["category"] != None:
                member["category"] = member["category"].name
        # print(type(temp_dict))
        # print(temp_dict)
        with open(self.filepath, "w+") as file:
            json.dump(temp_dict, file)
            file.close()


Transactions = AllTransactions()
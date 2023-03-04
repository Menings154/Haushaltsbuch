import json

class StdClass:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.filepath = ""
   
    def add_member(self, member):
        self.members.append(member)
        self.save()

    def save(self):
        member_temp = []
        # for member in self.members:
        #     try:
        #         cat_name_temp = member["category"].name
        #         temp_dic = member.__dict__.copy()
        #         temp_dic["category"] = cat_name_temp
        #         member_temp.append(temp_dic)
        #     else ValueError:
        member_temp = [member.__dict__ for member in self.members]
        temp_dict = self.__dict__.copy()
        temp_dict["members"] = member_temp
        with open(self.filepath, "w+") as file:
            json.dump(temp_dict, file)
            file.close()

    def load(self):
        with open(self.filepath, "r") as file:
            self.__dict__ = json.load(file)
            all_members = self.members
            file.close()
        return all_members  # das eigentliche Laden muss dann in jeder klasse selbst passieren

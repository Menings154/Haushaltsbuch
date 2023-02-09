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
        member_temp = [member.__dict__ for member in self.members]
        temp_dict = self.__dict__
        temp_dict["members"] = member_temp
        with open(self.filepath, "w+") as file:
            json.dump(temp_dict, file)
            file.close()

    def load(self):
        with open(self.filepath, "r") as file:
            self.__dict__ = json.load(file)
            all_members = self.members
            # all_members_temp = []
            file.close()
        return all_members  # das eigentliche Laden muss dann in jeder klasse selbst passieren
            # for member in all_members:
            #     # wie mache ich das hier?
            #     temp = Transaction(member['name'], member['value'], member['day'], member['month'], member['year'])
            #     all_members_temp.append(temp)
            # self.members = all_members_temp
            # file.close()


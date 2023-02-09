# import json
# import inspect
# from data_structure.Category import Category

# class Saver:
#     def __init__(self):
#         self.filepath = ""

#     def load(self):
#         with open(self.filepath, "r") as file:
#             self.__dict__ = json.load(file)
#             file.close()

#     def save(self):
#         with open(self.filepath, "w+") as file:
#             json.dump(self.__dict__, file)
#             file.close()


# class CollectionSaver:
#     def __init__(self):
#         self.filepath = ""
#         self.members = []
#         self.Object = ""
#         self.initializer_args = []

#     def load(self):
#         temp_obj = self.Object
#         with open(self.filepath, "r") as file:
#             self.__dict__ = json.load(file)
#             all_members = self.members
#             all_members_temp = []
#             keys = inspect.signature(self.Object.__init__)
#             for member in all_members:
#                 if len(keys) == 1:
#                     temp = self.Object(member[keys[0]])
#                 elif len(keys) == 2:
#                     temp = self.Object(member[keys[0]], member[keys[1]])
#                 elif len(keys == 5):
#                     temp = self.Object(member[keys[0]], member[keys[1]], member[keys[2]], member[keys[3]], member[keys[4]])
#                 else:
#                     raise ValueError("Initializer has not a standart amount of arguments!")
#                 all_members_temp.append(temp)
#             self.members = all_members_temp
#             file.close()
#         self.Object = temp_obj
        
#     def save(self):
#         print(self.members)
#         object_temp = [trns.__dict__ for trns in self.members]
#         temp_dict = self.__dict__.copy()
#         temp_dict["members"] = object_temp
#         temp_dict["Object"] = None
#         for member in temp_dict["members"]:
#             if type(member["category"]) == Category:
#                 member["category"] = member["category"].name
#         # print(type(temp_dict))
#         # print(temp_dict)
#         with open(self.filepath, "w+") as file:
#             json.dump(temp_dict, file)
#             file.close()
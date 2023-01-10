import json

class Saver:
    def __init__(self):
        self.filepath = ""

    def load(self):
        file = open(self.filepath, "r")
        self.__dict__ = json.load(file)
        file.close()

    def save(self):
        file = open(self.filepath, "w")
        json.dump(self.__dict__, file)
        file.close()
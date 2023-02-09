import re
import json

class Namer:
    def __init__(self):
        self.lut = {}
        self.filepath = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\saved objects\Namer.json"

    def load(self):
        with open(self.filepath, "r") as file:
            self.lut = json.load(file)
            file.close()

    def save(self):
        with open(self.filepath, "w") as file:
            json.dump(self.lut, file)
            file.close()

    def name(self, text):
        for regex in self.lut.keys():
            result = re.search(regex, text)
            if result != None:
                return self.lut[regex]
        return self.new_name(text)
    
    def new_name(self, text):
        print("Transaction couldn't be recognized.")
        print("Please give the following transaction a name.")
        print(text)
        name = input()
        print("Also please give the transaction a regex.")
        regex = input()
        self.lut[regex] = name
        self.save()
        return name

NamerInstance = Namer()
NamerInstance.load()
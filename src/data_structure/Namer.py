import re

class Namer:
    def __init__(self):
        self.lut = {}

    def load(self):
        pass

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
        return name

NamerInstance = Namer()
NamerInstance.load()
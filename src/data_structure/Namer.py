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
                print("Please check the Mapping")
                while True:
                    print("Text: ", text, "> mapping: ", self.lut[regex])
                    temp = input("true or false?")
                    if temp == "true":
                        return self.lut[regex]
                    elif temp != "false":
                        print('The answer was neither "true" nor "false"')
                    else:
                        break
        return self.new_name(text)
    
    def new_name(self, text):
        print("Transaction couldn't be recognized.")
        print("Please give the following transaction a name.")
        print(text)
        name = input()
        print("Also please give the transaction a regex.")
        while True:
            regex = input()
            try:
                if re.search(regex, text) is not None:
                    break
                else:
                    print("Regex: ", regex, "could not be found in the text...", text, "Please enter a new regex.")
            except re.error:
                print("This regex was wrong.")

        self.lut[regex] = name
        self.save()
        return name

NamerInstance = Namer()
NamerInstance.load()
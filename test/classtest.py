class Parent:
    def __init__(self, name):
        self.member =  []

    def print_hi(self):
        print('hi from parent class')
        print(self.member)
        self.speak()
    
    def speak(self):
        print("Parent")

class child(Parent):
    def __init__(self, name):
        super().__init__(name)
        self.name = "child"
        self.member = []

    def print_hi(self):
        super().print_hi()
        print(self.name)
    
    def speak(self):
        print("Child")


test = child("DiesName")
test.member.append('hi')
test.print_hi()

print(test.member)


# # dic = {'a': 1}

# # test = dic.copy()
# # test['a'] = 'penis'
# # print(test)
# # print(dic)

# import re

# text = """Überweisungsauftrag                                                 337,51 S
#               Frank Zenz
#               Autoversicherung + Baguettes TAN:760771 IBAN: DE525746
#               01170004101001 BIC: GENODED1NWD"""

# print(re.search('Autoversicherung', text))
# print(re.search('jj', text))


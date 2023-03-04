# class Parent:
#     def __init__(self, name):
#         self.name = name
#     def print_hi(self):
#         print('hi from parent class')

# class child(Parent):
#     def __init__(self, name):
#         super().__init__(name)

#     def print_hi(self):
#         super().print_hi()

# test = child("DiesName")
# test.print_hi()
# print(test.name)

# # dic = {'a': 1}

# # test = dic.copy()
# # test['a'] = 'penis'
# # print(test)
# # print(dic)

import re

text = """Überweisungsauftrag                                                 337,51 S
              Frank Zenz
              Autoversicherung + Baguettes TAN:760771 IBAN: DE525746
              01170004101001 BIC: GENODED1NWD"""

print(re.search('Autoversicherung', text))
print(re.search('jj', text))
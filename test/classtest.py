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

text = 'hallo'

print(re.search('ll', text))
print(re.search('jj', text))
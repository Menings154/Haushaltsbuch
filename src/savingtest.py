from data_structure import *

test_trns = Transaction.Transaction(0, 0, 0, 0, 0)
test_category = Category.Category('test')
#print(test_category.__dict__)
test_category.add_member(test_trns)
print("finish")
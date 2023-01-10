from Saver import Saver

test = Saver()
test.filepath = "savetest.json"

# test.method = 'first_test'
# test.method2 = 4

# test.save()

test.load()
print(test.method)
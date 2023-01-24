from data_structure import *
from reading.vr_bank_kontoauszug_reader import VRReader

path = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202201\20220131 Kontoauszug.pdf"

Reader = VRReader(path)

test_name = Namer.NamerInstance.name(Reader.output[0][0])

test_trns = Transaction.Transaction(name=test_name, value=Reader.output[0][1], day=Reader.output[0][2], month=Reader.output[0][3], year=Reader.output[0][4])


print("Categorizer lut >", Categorizer.CategorizerInstance.lut)

test_trns.add_category(Categorizer.CategorizerInstance.categorize(test_trns))

# print(test_trns.category)
print(Categorizer.CategorizerInstance.lut)

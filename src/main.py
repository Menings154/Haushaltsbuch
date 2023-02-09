from data_structure import *
from reading.vr_bank_kontoauszug_reader import VRReader

path = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202201\20220131 Kontoauszug.pdf"

Reader = VRReader(path)

for i in range(2):
    test_name = Namer.NamerInstance.name(Reader.output[i][0])
    test_trns = Transaction.Transaction(name=test_name, 
                                        value=Reader.output[i][1],
                                        day=Reader.output[i][2],
                                        month=Reader.output[i][3],
                                        year=Reader.output[i][4])
    test_trns.add_category(Categorizer.CategorizerInstance.categorize(test_trns))
    print(test_trns.category)
    print(Categorizer.CategorizerInstance.lut)
    print([member.name for member in Category.Categories.members])

# print("Categorizer lut >", Categorizer.CategorizerInstance.lut)


# print(test_trns.category)
# print(Categorizer.CategorizerInstance.lut)
# print([member.name for member in Category.Categories.members])
# nun müssen die monate und so hinzugefüft werden

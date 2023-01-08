from data_structure import *
from reading.vr_bank_kontoauszug_reader import VRReader

path = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202201\20220131 Kontoauszug.pdf"

Reader = VRReader(path)

test_name = Namer.NamerInstance.name(Reader.output[0][0])

test_name_2 = Namer.NamerInstance.name(Reader.output[0][0])
print(test_name)
print(test_name_2)

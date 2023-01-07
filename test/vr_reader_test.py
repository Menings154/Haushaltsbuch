from reading.vr_bank_kontoauszug_reader import VRReader

path = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202201\20220131 Kontoauszug.pdf"
test = VRReader(path)
print(test.alter_Kontostand)
print(test.neuer_Kontostand)
print(len(test.all_trnsctn))
for i in test.all_trnsctn:
    print(i)
print(len(test.all_trns_dates))
print(test.all_trns_dates)
print(test.all_trns_values)
print(test.year)
print(len(test.output))
for i in test.output:
    print(i)
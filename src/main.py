from data_structure import *
from reading.vr_bank_kontoauszug_reader import VRReader

path = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202201\20220131 Kontoauszug.pdf"
path2 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202202\4107008_2022_Nr.002_Kontoauszug_vom_28.02.2022_20221130073537.pdf"
path3 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202203\4107008_2022_Nr.003_Kontoauszug_vom_01.04.2022_20221130073535.pdf"
path4 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202204\4107008_2022_Nr.004_Kontoauszug_vom_30.04.2022_20221130073533.pdf"
path5 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202205\4107008_2022_Nr.005_Kontoauszug_vom_31.05.2022_20221130073530.pdf"

Reader = VRReader(path5)

def read(reader):
    spmonth = SpecificMonth.SpecificMonth(name=str(reader.month)+str(reader.year), 
                                          month=reader.month, year=reader.year) # hier drüber muss ich mir vielleicht noch gedanken machen
    spmonth.add_start_balance(reader.alter_Kontostand)
    spmonth.add_final_balance(reader.neuer_Kontostand)
    for count, value in enumerate(reader.output):
        name = Namer.NamerInstance.name(value[0])
        trnsctn = Transaction.Transaction(name=name, value = value[1],
                                          day=value[2], month=value[3],
                                          year=value[4])
        category = Categorizer.CategorizerInstance.categorize(trnsctn)
        category.add_member(trnsctn)
        trnsctn.add_category(category.name)
        trnsctn.save()

        for member in Day.Days.members:
            if member.day == trnsctn.day:
               member.add_member(trnsctn)
        for member in Month.Months.members:
            if member.month == trnsctn.month:
                member.add_member(trnsctn)
        for member in Year.Years.members:
            if member.year == reader.year:
                member.add_member(trnsctn)

        DayOfTheWeek.add_to_day_of_the_week(trnsctn=trnsctn)
        spmonth.add_member(trnsctn=trnsctn)
    return

read(reader=Reader)
print('finished')
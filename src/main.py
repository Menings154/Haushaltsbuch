from data_structure import *
from reading.vr_bank_kontoauszug_reader import VRReader

path = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202201\20220131 Kontoauszug.pdf"
path2 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202202\4107008_2022_Nr.002_Kontoauszug_vom_28.02.2022_20221130073537.pdf"
path3 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202203\4107008_2022_Nr.003_Kontoauszug_vom_01.04.2022_20221130073535.pdf"
path4 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202204\4107008_2022_Nr.004_Kontoauszug_vom_30.04.2022_20221130073533.pdf"
path5 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202205\4107008_2022_Nr.005_Kontoauszug_vom_31.05.2022_20221130073530.pdf"
path6 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202206\4107008_2022_Nr.006_Kontoauszug_vom_01.07.2022_20221130073528.pdf"
path7 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202207\4107008_2022_Nr.007_Kontoauszug_vom_30.07.2022_20221130073525.pdf"
path8 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202208\4107008_2022_Nr.008_Kontoauszug_vom_31.08.2022_20221130073523.pdf"
path9 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202209\4107008_2022_Nr.009_Kontoauszug_vom_01.10.2022_20221130073520.pdf"
path10 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202210\4107008_2022_Nr.010_Kontoauszug_vom_31.10.2022_20221130073504.pdf"
path11 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202211\4107008_2022_Nr.011_Kontoauszug_vom_2022.11.30_20230311115358.pdf"
path12 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202212\4107008_2022_Nr.012_Kontoauszug_vom_2022.12.31_20230311115402.pdf"
path13 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202301\4107008_2023_Nr.001_Kontoauszug_vom_2023.01.31_20230311115406.pdf"

path14 = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202302\4107008_2023_Nr.002_Kontoauszug_vom_2023.02.28_20230311115410.pdf"

Reader = VRReader(path14)

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
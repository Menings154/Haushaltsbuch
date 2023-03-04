import re
from PyPDF2 import PdfReader

class VRReader(PdfReader):
    def __init__(self, path):
        super().__init__(path)
        self.regex_first_split = "\d\d\.\d\d.\s\d\d\.\d\d\."
        self.regex_Kontostand = "\d*\.*\d+,\d\d\sH?S?"
        self.alter_Kontostand = self.value_to_float(self.get_alter_Kontostand())
        self.neuer_Kontostand = self.value_to_float(self.get_neuer_Kontostand())
        self.all_trnsctn = self.get_all_trnsctn()
        self.all_trns_dates = self.get_all_trns_dates()
        self.all_trns_values = self.get_all_trns_values()
        self.year = self.get_year()
        self.month = self.get_month()
        self.output = self.get_output()
        # touple aus dates und trnsaction machen?

    def get_alter_Kontostand(self):
        text = self.pages[0].extract_text()
        regex_alter_Kontostand = "alter\sKontostand"
        alter_Kontostand = re.search(self.regex_Kontostand, 
            re.split(regex_alter_Kontostand, 
                re.split(self.regex_first_split, text)[0])[1])[0][:-2]
        return alter_Kontostand

    def get_neuer_Kontostand(self):
        text = self.pages[-2].extract_text()
        regex_neuer_Kontostand = "neuer\sKontostand"
        neuer_Kontostand = re.search(self.regex_Kontostand, 
            re.split(regex_neuer_Kontostand, 
                re.split(self.regex_first_split, text)[-1])[1])[0][:-2]
        return neuer_Kontostand

    def get_all_trnsctn(self):
        regex_cut_last = "Übertrag auf "
        all_trnsctn = []
        for page in self.pages[:-1]:
            text = page.extract_text()
            split = re.split(self.regex_first_split, text)
            for part in split[1:]:
                rslt = part.find(regex_cut_last)
                if rslt!=-1:
                    part = part[:rslt]
                rslt = part.find("neuer Kontostand")
                if rslt!=-1:
                    part = part[:rslt]
                all_trnsctn.append(part)
        return all_trnsctn

    def get_all_trns_dates(self):
        all_dates_temp = []
        all_dates = []
        for page in self.pages[:-1]:
            text = page.extract_text()
            all_dates_temp += re.findall(self.regex_first_split, text)
        for date in all_dates_temp:
            all_dates.append(date[:5])
        return all_dates

    def get_all_trns_values(self):  # diese Methode vielleicht überdenken
        all_values = []
        for trns in self.all_trnsctn:
            value_temp = re.search(self.regex_Kontostand, trns)[0]
            if value_temp[-1] == 'S':
                value_temp = '-' + value_temp
            all_values.append(self.value_to_float(value_temp[:-2]))
        return all_values

    def value_to_float(self, value):
        value = value.replace('.', '').replace(',', '.')
        return float(value)

    def get_year(self):
        regex_year = "\d+/\d\d\d\d"
        text = self.pages[0].extract_text()
        return int(re.search(regex_year, text)[0][-4:])
    
    def get_month(self):
        regex_month = "\d+/\d\d\d\d"
        text = self.pages[0].extract_text()
        return int(re.search(regex_month, text)[0][:-5])

    def get_output(self):
        output = []
        for i in range(len(self.all_trnsctn)):
            output.append((self.all_trnsctn[i], self.all_trns_values[i], int(self.all_trns_dates[i][:2]), int(self.all_trns_dates[i][3:]), self.year))
        return output


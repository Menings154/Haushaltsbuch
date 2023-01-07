from PyPDF2 import PdfReader
import re

# path = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202201\20220131 Kontoauszug.pdf"

# reader = PdfReader(path)
# number_of_pages = len(reader.pages)
# page = reader.pages[0]
# text = page.extract_text()
# print(text)
# #new_text = text.split("\n")
# #print(new_text)

# # write to file to give better overview
# # with open(r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\src\reading\test.txt", 'w') as file:
# #     for part in new_text:
# #         file.write(part)
# #         file.write('\n')

# regex = "\d\d\.\d\d.\s\d\d\.\d\d\."

# result = re.split(regex, text)
# print(result[0])
# # print(result[1])

# #print(re.findall(regex, text))

# regex2 = "\d\.\d\d\d\,\d\d\sH"
# regex3 = "alter\sKontostand"
# new = re.split(regex3, result[0])
# print(new[1])
# print(re.search(regex2, result[0])[0][:-2])


# # erster eintrag einfach nicht beachten

# # ====================== how to cut last transaction of a page =====================
# regex2 = "Übertrag auf "

# testtxt = result[-1]
# print("before")
# print(testtxt)
# rslt = testtxt.find(regex2)
# if rslt != -1:
#     testtxt = testtxt[:rslt]
# print("after")
# print(testtxt)

# # Kontostand am anfang vom Monat herausfinden
# # vielleicht ist die zweite Variante sicherere
# regex2 = "\d\.\d\d\d\,\d\d\sH"
# regex3 = "alter\sKontostand"
# new = re.split(regex3, result[0])
# print(new[1])
# print(re.search(regex2, result[0])[0][:-2])

#text = "hi ha ho"
#print(text.replace("ha", ""))

dates = ['03.01', '03.01', '04.01', '04.01', '04.01', '05.01', '06.01', '12.01', '17.01', '18.01', '18.01', '20.01', '20.01', '21.01', '21.01', '21.01', '24.01', '24.01', '24.01', '27.01', '31.01']
for i in range(len(dates)):
    print(dates[i][2:])
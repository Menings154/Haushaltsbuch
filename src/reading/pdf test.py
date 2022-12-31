from PyPDF2 import PdfReader

path = r"C:\Users\Benja\Code\Python\Finanzen\Haushaltsbuch\data\input\202201\20220131 Kontoauszug.pdf"

reader = PdfReader(path)
number_of_pages = len(reader.pages)
page = reader.pages[-2]
text = page.extract_text()

new_text = text.split("\n")
print(new_text)
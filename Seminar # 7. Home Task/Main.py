from os.path import exists
# импортирует метод записи в табличный формат CSV
from CSV_creating import csv_creating
from Writing import writing_scv  # записывает через запятыую табличный формат CSV
from Writing import writing_txt  # записывает табличный формат TXR


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    csv_creating()

writing_scv()
writing_txt()

from reader import csv_reader
from cleaner import cleaner
import pandas as pd

csv_file = open('receita.csv', 'r')
dict_list = csv_reader(csv_file)
file_cleaned = cleaner(dict_list)
imports = pd.DataFrame(file_cleaned)
export_csv = imports.to_csv(r'C:\Users\CalebeLadis\PycharmProjects\csv-reader\receita2.csv', index=None, header=True)

from reader import csv_reader
from cleaner import cleaner

csv_file = open('receita.csv', 'r')
dict_list = csv_reader(csv_file)
file_cleaned = cleaner(dict_list)

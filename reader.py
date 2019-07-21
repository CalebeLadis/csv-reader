import csv
# TODO: Save dictionarie list as a json file


def csv_reader(csv_file):
    with csv_file:
        reader = csv.reader(csv_file, delimiter='@')
        is_header = True
        header = []
        element = []
        dic = {}

        for row in reader:
            if is_header:
                header = row
                is_header = False
            else:
                for item in row:
                    index = row.index(item)
                    el_column = header[index]
                    dic[el_column] = item
                element.append(dic)
                dic = {}
    return element

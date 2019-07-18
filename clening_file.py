import csv
import json
f = open('receita.csv', 'r')

with f:
    reader = csv.reader(f, delimiter='@')
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
    # TODO: Save dictionarie list as a json file
    # with open('json.json', 'w') as new_file:
    #     data = ''
    #     for item in element:
    #         temp = str(item)
    #         data += (temp + ',')
    #     print(data)
    #     json.dump(data, new_file)





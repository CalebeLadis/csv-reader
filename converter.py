file = open('receita.csv', 'r')

first_line = file.readline()
new_line = first_line.replace('@', ',')

keys = []
word = ''
second_backspace = False
blank = 0
previous = ''
#Getting columns names
for x in new_line:
    if x == ' ':
        blank += 1
        if blank > 1 and previous == ' ':
            second_backspace = True
    if not second_backspace and x != ',' and x != '':
        word += x
    elif x == ',' or (second_backspace and x == ','):
        keys.append(word)
        word = ''
        second_backspace = False
        blank = 0
    previous = x

# TODO: Implement condition that take off all empty single quotation marks from the list
# for e in range(len(keys)):
#     if keys[e] == '':

for e in range(len(keys)):
    keys[e] = keys[e][:-1]
print(keys)
file.close()
with open('cobol.copy','r') as file:
    file_data = file.readlines()    

file_code = [x[6:-11] for x in file_data]
new_code = []
comma = ''

for line in file_code:
    new_code.append(line)
    space_index = line.find('05')
    if space_index != -1:
        str_spaces = [' ']*space_index
        str_spaces.append('05  FILLER PIC X(01) VALUE \',\'.')
        new_code.append(comma.join(str_spaces))
        new_code.append(' ')
    space_index = line.find('10')
    if space_index != -1:
        str_spaces = [' ']*space_index
        str_spaces.append('10  FILLER PIC X(01) VALUE \',\'.')
        new_code.append(comma.join(str_spaces))
        new_code.append(' ')
    space_index = line.find('15')
    if space_index != -1:
        str_spaces = [' ']*space_index
        str_spaces.append('15  FILLER PIC X(01) VALUE \',\'.')
        new_code.append(comma.join(str_spaces))
        new_code.append(' ')

for line in new_code:
    print(line)
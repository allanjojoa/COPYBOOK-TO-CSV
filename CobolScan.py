
# coding: utf-8

# In[235]:


with open('cobol.copy','r') as file:
    file_data = file.readlines()    


# In[236]:


file_code = [x[6:-11] for x in file_data]
new_code = []
csv_header_code = []
comma = ''
new_line = '\n'


# In[237]:


def get_code_file():    
    file_code = [x[6:-11] for x in file_data]


# In[238]:


def get_new_code(level_number):
    space_index = line.find(level_number)
    find_pic = line.find('PIC')
    if space_index != -1 and find_pic != -1:
        #Header File
        var_name = line.split(' ')[space_index+2].replace('.','')
        code_str = line
        csv_header_code[-1] = code_str[:find_pic]+'PIC X('+str(len(var_name))+') VALUE'
        csv_header_code.append((' '*find_pic)+'\''+var_name+'\'.')
        #CSV File
        str_spaces = [' ']*space_index
        str_spaces.append(level_number+'  FILLER PIC X(01) VALUE \',\'.')
        new_code.append(comma.join(str_spaces))


# In[239]:


for line in file_code:
    csv_header_code.append(line)
    new_code.append(line)
    get_new_code('05')
    get_new_code('10')
    get_new_code('15')


# In[240]:


code_str = new_line.join(new_code)
with open('cobol-csv.copy','w') as file:
    file.writelines(code_str)


# In[241]:


csv_str  = new_line.join(csv_header_code)
with open('cobol-csv-header.copy','w') as file:
    file.writelines(csv_str)


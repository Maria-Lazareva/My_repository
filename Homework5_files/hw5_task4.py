russian = {
           'One' : 'Один',
           'Two' : 'Два',
           'Three' : 'Три',
           'Four' : 'Четыре'
           }

new_file = []
with open('mydict.txt', 'r') as file:
    for i in file:
        i = i.split(' ', 1)
        new_file.append(russian[i[0]] + '  ' + i[1])
    print(new_file)

with open('mydict_new.txt', 'w') as file_2:
    file_2.writelines(new_file)

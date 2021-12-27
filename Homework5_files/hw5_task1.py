# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open('test.txt', 'w') as new_file:

    line = input('Введите текст: \n')
    while line:
        new_file.write(f'{line}\n')
        line = input('Введите текст: \n')
        if not line:
            break


with open('test.txt') as new_file:

    content = new_file.readlines()
    print(content)



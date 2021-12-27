# 2. Создать текстовый файл (не программно), сохранить в нем несколько
# строк, выполнить подсчет количества строк, количества слов в каждой строке.

# Вариант 1:
with open('new_test_file.txt') as file:
    content = file.read()
    print(f'Содержимое файла: \n {content}')
with open('new_test_file.txt') as file:
    content = file.readlines()
    print(f'Количество строк в файле - {len(content)}')
with open('new_test_file.txt') as file:
    content = file.readlines()
    str_count = 0
    for num, line in enumerate(content):
        str_count +=1
        wordsc = len(line.split())
        print(f'№{num + 1} - {wordsc} слов')
    print(f'{str_count} строк')
    # for i in range(len(content)):
    #     print(f'Количество символов {i + 1}-ой строки {len(content[i])}')
with open('new_test_file.txt') as file:
    content = file.read()
    content = content.split()
    print(f'Общее количество слов - {len(content)}')


# Вариант 2:
# with open('New_test_file.txt') as file:
#     lines = file.readlines()
#     str_count = 0
#     for num, line in enumerate(lines):
#         str_count += 1
#         wordsc = len(line.split())
#         print(f'№{num + 1} - {wordsc} words')
#     print(f'{str_count} strings')


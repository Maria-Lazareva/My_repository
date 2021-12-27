# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
#

with open('file_5.txt', 'w+') as file:
    line = input('Введите цифры через пробел \n')
    file.writelines(line)
    my_numb = line.split()
    print(sum(map(int, my_numb)))

# Вариант 2
# import random
#
# with open('file_5_2.txt', 'w') as file:
#     for _ in range(30):
#         file.write(f'{random.randint(0, 10)}')
#
# with open('file_5_2.txt') as file:
#     nums_str = file.read().split()
#     sum = 0
#     for num in nums_str:
#         sum += int(num)
#
#
# print(sum)
#

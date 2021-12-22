# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
# не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

# Вариант 1
# Часть а:
from itertools import count

print("Итератор целых чисел, начиная с указанного ")
n = int(input("Введите целое число: "))


for i in count(n):
    if i < 3 or i > 10:
        break
    else:
        print(i, end=' ')

# Часть б:
from itertools import cycle

list = [5, 3, 3, 1, 0, 4, 2, 4, 7, 3]
count1 = 0
for i in cycle(list):
    if count1 > 35:
        break
    else:
        print(i, end=' ')
        count1 += 1


# Эталонный вариант:
#
# from itertools import cycle, count
#
# n = 100
# numbers_list = [el for el in  range(5)]
# counter = count()
# cycler = cycle(numbers_list)
# print([next(counter) for el in range(n)])
# print([next(cycler) for el in range(n)])
#
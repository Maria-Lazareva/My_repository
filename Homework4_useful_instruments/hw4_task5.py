# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

list1 = [el for el in range(100, 1001) if el % 2 == 0]
print(list1)
from functools import reduce
def my_func(el_prev, el):
    return el_prev * el
print(reduce(my_func, list1))

# Вариант 2
# from functools import reduce
#
# numbers_list = [el for el in range(100, 1001, 2)]
# print(reduce(lambda a, b: a * b, numbers_list))
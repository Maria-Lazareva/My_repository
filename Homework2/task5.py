# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел. У пользователя необходимо запрашивать новый элемент
# рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
# элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].

# Вариант 1.
# rating_num = int(input('Введите новый элемент рейтинга: '))
# my_list = [7, 5, 3, 3, 2]
# counting = my_list.count(rating_num)
# for elem in my_list:
#     if counting > 0:
#         i = my_list.index(rating_num)
#         my_list.insert(i+counting, rating_num)
#         break
#     else:
#         if rating_num > elem:
#             el = my_list.index(elem)
#             my_list.insert(el, rating_num)
#             break
#         elif rating_num < my_list[len(my_list) - 1]:
#             my_list.append(rating_num)
# print(my_list)

# Вариант 2
my_list = [9, 7, 5, 3, 3, 2]
rating_num = int(input('Введите новый элемент рейтинга: '))
added = False
for index, el in enumerate(my_list):
    if rating_num > el:
        my_list.insert(index, rating_num)
        added = True
        break

if not added:
    my_list.append(rating_num)

print(my_list)
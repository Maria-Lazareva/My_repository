#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный
# символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
#
#
# Вариант 1. Работает.
#
def calc_sum(*nums):
    sum = 0
    flag = False
    for num in nums:
        try:
            if num:
                sum += int(num)
        except ValueError:
            flag = True
            break
    return sum, flag

gsum = 0

while True:
    numbers_string = input('Введите числа через пробел либо * чтобы выйти: ').split(' ')
    sum, stop_flag = calc_sum(*numbers_string)
    gsum += sum
    print(f'сумма:  {gsum}')

    if stop_flag:
        break

#
#
# Вариант 2. По аналогии с решением:
# def myfunc(nums_str, stop):
#     nums_list = nums_str.split(' ')
#     sum_list = 0
#     for i in nums_list:
#         if i == stop:
#             break
#         sum_list += int(i)
#
#     return sum_list
#
#
# stopper = '*'
# finished = False
# s = 0
# while not finished:
#     nums_str_user = input('Введите числа через пробел либо * чтобы выйти: ')
#     s += myfunc(nums_str_user, stopper)
#     finished = stopper in nums_str_user
#     print(f'Сумма = {s}')

# Вариант 3:

# def func_try(*numbers):
#     result = 0
#     while True:
#         numbers = input('Введите числа через пробел либо * чтобы выйти: ').split(' ')
#         for i in numbers:
#             try:
#                 if i == '*':
#                     print(f'Сумма равна  {result}.')
#                     return
#                 else:
#                     result += int(i)
#             except ValueError:
#                 print('Введите числа через пробел либо * чтобы выйти: ')
#         print(f'Сумма равна {result}')
#
# func_try()



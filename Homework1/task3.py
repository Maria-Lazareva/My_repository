# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

string_1 = input('Введите цифру от 1 до 9: ')
string_2 = string_1 * 2
string_3 = string_1 * 3
result = int(string_1) + int(string_2) + int(string_3)
print('Результат: ' + str(result))

# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.


class List_Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        # self.my_list = [int(i) for i in input('Enter numbers separated by a space ').split()]
        # values = int(input('Enter a number and press Enter - '))
        # self.my_list.append(values)
        while True:
            try:
                values = int(input('Enter a number one by one - '))
                self.my_list.append(values)
                print(f'Current list - {self.my_list} \n ')
            except:
                print(f"Incorrect number. Cannot be str or bool")
                yes_or_no = input(f'Try again? Y/N:  ')

                if yes_or_no == 'Y' or yes_or_no == 'y':
                    print(test.my_input())
                elif yes_or_no == 'N' or yes_or_no == 'n':
                    return f'The end. '
                else:
                    return f'The end'

test = List_Error(1)
print(test.my_input())



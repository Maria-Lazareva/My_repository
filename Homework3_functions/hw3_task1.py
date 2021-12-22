#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def mycalc(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя.'
    except ValueError:
        return 'No value'


print(mycalc((int(input('First number: '))), (int(input('Second number: ')))))





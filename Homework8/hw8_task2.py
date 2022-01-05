# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class Zero_Division:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    @staticmethod
    def divide_by_zero(dividend, divisor):
        try:
            return (dividend / divisor)
        except:
            return (f"Cannot divide by zero")


divide = Zero_Division(90, 10)
print(Zero_Division.divide_by_zero(55, 0))
print(Zero_Division.divide_by_zero(66, 0.1))
print(divide.divide_by_zero(199, 0))


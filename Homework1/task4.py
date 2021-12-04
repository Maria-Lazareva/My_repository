#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


number = int(input('Введите целое положительное число: '))
desired_number = -1
while number >= 1:
    maxn = number % 10
    number //= 10
    if maxn > desired_number:
        desired_number = maxn
print(desired_number)

def salary_module():
    try:
        time = float(input('Выработка в часах: '))
        salary = float(input('Ставка в час в рублях: '))
        bonus = float(input('Премия в рублях: '))
        res = time * salary + bonus
        print(f'Заработная плата сотрудника  {res}')
    except ValueError:
        return print('Введите числовое значение')
salary_module()


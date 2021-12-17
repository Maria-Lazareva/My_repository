#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

def pers_data(name, lastname, yearb, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {yearb}'
                 f'Город проживания: {city} Email: {email} Телефон: {phone}')


pers_data(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    yearb=input('Год рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('тел.: '),
)


# # Вариант 2
# def pers_data(**kwargs):
#     return list(kwargs.values())
#
# print(pers_data(name=input('Имя: '),
#                     lastname=input('Фамилия: '),
#                     yearb=input('Год рождения: '),
#                     city=input('Город проживания: '),
#                     email=input('email: '),
#                     phone=input('тел.: ')))
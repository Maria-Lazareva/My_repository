# 3. Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников имеет
# оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# Вариант 1:
#
# empl = {'Ivanov': 30000, 'Pavlov': 80000, 'Petrushin': 201}
# with open('employees.txt', 'w') as file:
#
#     for last_name, salary in empl.items():
#         file.write(last_name + ': ' + str(salary) + "\n")
#
# summa = 0
# count = 0
# persons = []
# with open("employees.txt", "r") as file_obj:
#     for line in file_obj:
#         print(line, end="")
#         tokens = line.split(':')
#         if int(tokens[1]) <= 20000:
#             persons.append(tokens[0])
#         summa += int(tokens[1])
#         count += 1
# result = summa / count
# print(f"Person's name: {persons}")
# print(f"Average salary: {result}")


# # Вариант 2:
with open('employees.txt', encoding="utf-8") as file:
    file_lines = file.readlines()
    empl_dict = {}
    sum_sal = 0
    for line in file_lines:
        empl_info = line.split()
        empl_dict.update({empl_info[0]: int(empl_info[1])})
        sum_sal += int(empl_info[1])
avg_salary = sum_sal / len(empl_info)
print(f'Average salary is {avg_salary}')

for key, value in empl_dict.items():
    if value < 20000:
        print(f'{key}: {value}')
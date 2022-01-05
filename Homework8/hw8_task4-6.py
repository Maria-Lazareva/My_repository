# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.




class OrgTech:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Name of device': self.name, 'Price per unit': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'{self.name} price: {self.price} quantity: {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        try:
            unit = input(f'Enter name of device: ')
            unit_p = int(input(f'Enter price per unit: '))
            unit_q = int(input(f'Enter quantity: '))
            dict = {'Model of device ': unit, 'Price per unit ': unit_p, 'Quantity ': unit_q}
            self.my_unit.update(dict)
            self.my_store.append(self.my_unit)
            print(f'Current list: \n {self.my_store}')
        except:
            return f'Input Error'

        print(f'to quit press Q, to continue press Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Full store -\n {self.my_store_full}')
            return f'Exit'
        else:
            return OrgTech.reception(self)


class Printer(OrgTech):
    def to_print(self):
        return f'to print {self.numb} times'


class Scanner(OrgTech):
    def to_scan(self):
        return f'to scan {self.numb} times'


class Xerox(OrgTech):
    def to_xerox(self):
        return f'to copy  {self.numb} times'


unit_1 = Printer('Sony', 600, 4, 19)
unit_2 = Scanner('Philips', 990, 2, 50)
unit_3 = Xerox('Samsung', 40, 4, 33)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_xerox())




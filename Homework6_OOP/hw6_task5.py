# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
# атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск
# отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы
# должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Starting drawing")

class Pen(Stationary):
    def draw(self):
        print(f"Drawing with a pen {self.title}")

class Pencil(Stationary):
    def draw(self):
        print(f"Drawing with a pencil {self.title}")

class Handle(Stationary):
    def draw(self):
        print(f"Drawing with a handle {self.title}")


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

print(pen.draw())

print(pencil.draw())

print(handle.draw())
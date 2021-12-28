# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, colour, name, is_police=False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
         return f'{self.name} took off'
        # print('go')

    def stop(self):
         return f'{self.name} has stopped'

    def turn_right(self):
         print(f'{self.name} turned right')

    def turn_left(self):
        print(f'{self.name} turned left')

    def show_speed(self):
        return f'Current speed of {self.name} is {self.speed}'

class TownCar(Car):
    def __init__(self, speed, colour, name, is_police):
        super().__init__(speed, colour, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 60:
            print ("Speed limit > 60")
            # return f'Speed of {self.name} is higher than allowed for town car'
        # else:
        #     return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, colour, name, is_police=False):
        super().__init__(speed, colour, name, is_police=False)

class WorkCar(Car):
    def __init__(self, speed, colour, name, is_police=False):
        super().__init__(speed, colour, name, is_police=False)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 40:
            print("Speed limit > 40!")
            # return f'Speed of {self.name} is higher than allowed for a work car'

class PoliceCar(Car):
    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name, True)

    # def police(self):
    #     if self.is_police:
    #         return f'{self.name} is a police car'
    #     else:
    #         return f'{self.name} is not not a police car'
town = TownCar(100, "purple", "Town", False)
sport = SportCar(130, "red", "Sport")
work = WorkCar(44, "white", "Work")
police = PoliceCar(90, "blue", "Police")

town.show_speed()
work.show_speed()

work.speed = 39
work.show_speed()

town.turn_right()
police.turn_left()



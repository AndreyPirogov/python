import random


class Car:

    def __init__(self, name, color, is_police):
        self.speed = int(random.random() * 120)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        return self.speed


class TownCar(Car):

    def __init__(self, name, color):
        Car.__init__(self, name, color, False)

    def show_speed(self):
        if self.speed > 60:
            print(f"Привышение скорость")
        return self.speed


class SportCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color, False)


class WorkCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color , False)

    def show_speed(self):
        if self.speed > 40:
            print(f"Привышение скорости")
        return self.speed


class PoliceCar(Car):

    def __init__(self, name, color):
        super().__init__(name, color, True)


town = TownCar("Жигули", "Черный")
sport = SportCar("Aуди", "Красный")
work = WorkCar("Трактор", "Черный")
police = PoliceCar("Лада", "Синий")

list_auto = [town, sport, work, police]

for el in list_auto:
    print(el.name)
    print(el.color)
    print(el.speed)
    print(el.is_police)
    el.go()
    el.turn("налево")
    print(el.show_speed())
    el.stop()
    print("==============")
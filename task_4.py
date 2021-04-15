from abc import ABC, abstractmethod


class Repository:

    def __init__(self):
        self.rep = {}

    def add_technics(self, technics, count):
        if self.rep.get(technics.name) is None:
            self.rep.update({technics.name: int(count)})
        else:
            a = int(count) + int(self.rep.get(technics.name))
            self.rep.update({technics.name: a})

    def del_technics(self, technics, count):
        a = self.rep.get(technics)
        if a is None:
            print(f"Техника {technics.name} на складе не найдена")
        elif a - int(count) < 0:
            print(f"На складе только {a} едениц техники {technics.name} уточните запрос")
        else:
            self.rep.update({technics.name: (a - int(count))})


class OfficeEquipment(ABC):

    def __init__(self, name):
        self.name = name

    def turn_on(self):
        print(f"{self.name} включен.")

    def turn_of(self):
        print(f"{self.name} выключен")

    @abstractmethod
    def work(self):
        pass


class Printer(OfficeEquipment):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def work(self):
        print("Идет печать")


class Xerox(OfficeEquipment):

    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

    def work(self):
        print("Копирую")


class Copy(OfficeEquipment):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        pass


r = Repository()
p = Printer("принтер 1", "черный")
p_2 = Printer("принтер 2", "белый")
p_3 = Printer("принтер 3", "синий")
r.add_technics(p, 2)
r.add_technics(p, 4)
r.add_technics(p_2, 3)
r.add_technics(p_3, 4)

print(r.rep)


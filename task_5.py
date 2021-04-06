class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def __init__(self):
        super().__init__("Pen")

    def draw(self):
        print("Пишу ручкой")


class Pencil(Stationery):

    def __init__(self):
        super().__init__("Pencil")

    def draw(self):
        print("Рисую карандашом")


class Handle(Stationery):

    def __init__(self):
        super().__init__("Handle")

    def draw(self):
        print("Подчеркивая маркером")


list_station = [Stationery("Канцелярская принадлежность"), Handle(), Pencil(), Pen()]

for el in list_station:
    el.draw()

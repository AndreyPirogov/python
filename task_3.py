class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


director = Position("Иван", "Иванов", "директор", 100000, 10000)
work = Position("Петров", "Петр", "работник", 10000, 0)

print(director.get_full_name())
print(director.get_total_income())

print(work.get_full_name())
print(work.get_total_income())
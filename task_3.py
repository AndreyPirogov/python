class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        result_nucleus = self.nucleus - other.nucleus
        if result_nucleus > 0:
            return Cell(result_nucleus)
        else:
            print("Вычитание невозможно")
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):
        return Cell(self.nucleus // other.nucleus)

    def make_order(self, arg):
        string = ""
        index = 1
        for el in range(self.nucleus):
            if index < arg:
                string += "*"
                index += 1
            else:
                string += "*\n"
                index = 1
        return string


c_1 = Cell(10)
c_2 = Cell(22)
c_3 = Cell(15)

print((c_1 + c_2).nucleus)
print((c_1 - c_2).nucleus)
print((c_2 + c_1).nucleus)
print((c_3 * c_2).nucleus)
print((c_2 / c_1).nucleus)

print(c_1.make_order(3))
print(c_3.make_order(4))

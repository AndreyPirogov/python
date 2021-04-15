class Zero(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))
result = 0

try:
    if b == 0:
        raise Zero("Деление на ноль")
    result = a / b
    print(result)
except Zero as err:
    print(err)


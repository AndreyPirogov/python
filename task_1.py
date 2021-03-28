def calc(var_1, var_2):
    try:
        result = var_1 / var_2
    except ZeroDivisionError:
        return "Деление на ноль"
    return result


a = int(input("Введите числитель: "))
b = int(input("Введите знаминатель: "))

print(calc(a, b))

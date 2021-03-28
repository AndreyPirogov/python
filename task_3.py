def my_func(var_1, var_2, var_3):
    minimum = min(var_1, var_2, var_3)
    return (var_1 + var_2 + var_3) - minimum


a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

print(my_func(a, b, c))
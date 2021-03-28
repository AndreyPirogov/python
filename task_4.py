def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    power = abs(y)
    result = x
    for i in range(1, power):
        result = result * x
    return 1 / result


x = int(input("Первое число: "))
y = int(input("Второе число: "))

print(my_func_1(x, y))
print(my_func_2(x, y))
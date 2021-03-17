number = int(input("Введите число: "))

max_number = 0

while True:
    a = number % 10
    number = number // 10
    if a > max_number:
        max_number = a
    if number == 0:
        break
print(max_number)
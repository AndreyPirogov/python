import itertools

start = int(input("Начальное значение: "))
end = int(input("Конечное значение: "))

for el in itertools.count(start):
    if el > end:
        break
    else:
        print(el)

for el in itertools.cycle("QWE"):
    if start > end:
        break
    else:
        print(el)
        start += 1

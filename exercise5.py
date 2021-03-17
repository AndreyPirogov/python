proceeds = int(input("Введите выручку: "))

cost = int(input("Введите издержки: "))

profit = proceeds - cost

if profit >= 0:
    print("Компания работает без убытков")
    print(f"Рентабельность {profit / proceeds}")
    worker = int(input("Введите количество сотрудников: "))
    print(f"Прибыль на одного сотрудника: {profit / worker}")
else:
    print("Компания убыточная!")
result = int(input("Введите результат первого дня: "))
target = int(input("Введите цель: "))
day = 1

while True:
    if result >= target:
        print(f"на {day}-й день спортсмен достиг результата — не менее {target} км.")
        break
    else:
        result = result + (result / 10)
        day = day + 1

file = open("task_3.txt")
content = file.readlines()

sum_sal = 0
print("Зарплату меннее 20 000 имеют следующие сотрудники: ")

for el in content:
    name, sal = el.split()
    sum_sal += int(sal)
    if int(sal) < 20000:
        print(name)

print(f"Средняя заработная плата: {sum_sal / len(content)}")

file.close()
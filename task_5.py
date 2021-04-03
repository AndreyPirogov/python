content = input("Введите числа: ")
my_sum = 0

with open("task_5.txt", "w") as file:
    file.writelines(content)

with open("task_5.txt", "r") as file:
    new_content = file.read().split()
    for el in new_content:
        my_sum += int(el)

print(my_sum)

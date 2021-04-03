my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("task_4.txt", "r") as file:
    content = file.readlines()

with open("task_4_new.txt", "w") as file:
    for el in content:
        a, b, c = el.split()
        file.write(f"{my_dict.get(a)} {b} {c}\n")
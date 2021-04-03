file = open("task_1.txt", "w")

while True:
    content = input("Введите текст: ")
    if content == "":
        break
    else:
        file.write(content + "\n")
file.close()
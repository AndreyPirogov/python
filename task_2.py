count_str = 0
count_words = 0

with open("task_2.txt", "r") as file:
    for line in file:
        count_str += 1
        count_words += len(line.split())

print(f"Колчиество строк {count_str}, количество слов {count_words}")
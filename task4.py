user_str = input("Введите строку: ")

user_str_list = user_str.split()

for ind, el in enumerate(user_str_list):
    if len(el) < 10:
        print(f"{ind}) {el}")
    else:
        print(f"{ind}) {el[:10]}")


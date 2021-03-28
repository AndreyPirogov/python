def int_func(var):
    s = str(var)
    return s[0].upper() + s[1:len(s)]


def str_func(var):
    s = ""
    str_list = var.split()
    for el in str_list:
        s = s + int_func(el) + " "
    return s.rstrip()


print(int_func(input("Введите текст: ")))
print(str_func(input("Введите строку: ")))

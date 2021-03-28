def digit(arg):
    try:
        int(arg)
        return True
    except ValueError:
        return False


sum_list = []
chek = True
while chek:
    tmp = input("Введите число, для выхода введите : ")
    tmp_list = tmp.split(" ")
    for el in tmp_list:
        if el == "#":
            chek = False
        if digit(el):
            sum_list.append((int(el)))
    print(sum(sum_list))

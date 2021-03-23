# my_list = ["строка1", 12, 22, 1, "строка2", True, "строка3", False, 0]

my_list = []
print("Заполняем список, для выхода введите 'exit'")

while True:
    a = input("Введите элемент: ")
    if a == "exit":
        break
    else:
        my_list.append(a)


for el in range(len(my_list)):
    if el % 2 != 0:
        my_list[el-1], my_list[el] = my_list[el], my_list[el-1]


print(my_list)



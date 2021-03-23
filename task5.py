my_list = [7, 5, 3, 3, 2]

user_request = int(input("Введите число: "))
index = 0

for el in my_list:
    if user_request > el:
        my_list.insert(index, user_request)
        break
    elif index == (len(my_list) - 1):
        my_list.append(user_request)
        break
    else:
        index = index + 1

print(my_list)
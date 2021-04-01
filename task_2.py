def generation(var_list):
    count = -1
    for el in var_list:
        if var_list[count] < el and count > 0:
            yield el
        count += 1


my_old_list = [300, 1, 12, 44, 1, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [el for el in generation(my_old_list)]
print(my_new_list)

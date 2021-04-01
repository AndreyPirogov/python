from functools import reduce


def my_sum(prev_el, el):
    return prev_el * el


my_list = [el for el in range(100, 1001)]
print(reduce(my_sum, my_list))

def fact(n):
    count = 1
    for el in range(1, n + 1):
        count *= el
        yield count


for el in fact(4):
    print(el)

class DigitError(Exception):

    def __init__(self, txt):
        self.txt = txt


result_list = []
i = True

while i:
    try:
        a = input("Введите число, для выхода введите 'stop': ")
        if a.isdigit():
            result_list.append(a)
        else:
            raise DigitError("Вы ввели не число")
    except DigitError as err:
        print(err)
    finally:
        if a == "stop":
            i = False
            print(result_list)



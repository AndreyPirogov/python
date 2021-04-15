class Data:

    def __init__(self, data):
        self.data = data

    @staticmethod
    def valid_data(dd, mm, yy):
        if yy < 0:
            return False
        if mm < 0 or mm > 12:
            return False
        if dd < 0 or dd > 31:
            return False
        if mm % 2 == 0:
            if mm != 2 and dd > 30:
                return False
            if mm == 2 and dd > 28:
                return False
        return True

    @classmethod
    def pars_data(cls, data):
        my_yy = int(data[0:4])
        my_mm = int(data[4:6])
        my_dd = int(data[6:8])
        if cls.valid_data(dd=my_dd, mm=my_mm, yy=my_yy):
            print(f"Дата {data} корректна")
        else:
            print(f"Дата {data} не корректная")


d_1 = Data("20211201")
d_2 = Data("19010228")
d_3 = Data("20003311")

d_1.pars_data(d_1.data)
d_1.pars_data(d_2.data)
d_1.pars_data(d_3.data)


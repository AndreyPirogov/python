import time


class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        for el in self.__color:
            print(el)
            if el == "Красный" or el == "Зеленый":
                time.sleep(7)
            if el == "Желтый":
                time.sleep(2)


a = TrafficLight()
a.running()

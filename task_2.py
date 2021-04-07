class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, base_weight, depth):
        return self._width * self._length * base_weight * depth


road_1 = Road(20, 5000)
print(road_1.weight(25, 5))

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5

    def __init__(self, v):
        self.v = v


class Suit(Clothes):

    def consumption(self):
        return self.h * 2 + 0.3

    def __init__(self, h):
        self.h = h


c = Coat(42)
s = Suit(44)
print(c.consumption)
print(s.consumption())

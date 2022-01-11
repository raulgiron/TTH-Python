class Suma:
    def __init__(self, value1: int, value2: int):
        self.value1 = value1
        self.value2 = value2
        self.total = value1 + value2
        print(f"La suma de {self.value1} y {self.value2} es : {self.total}")


class Leon(Suma):
    def __init__(self):
        self.valor1 = 20
        self.valor2 = 50
        self.total_general = self.valor1 + self.valor2
        print(f"La suma de {self.valor1} y {self.valor2} es : {self.total_general}")
        super().__init__(self.valor2, 10)


nuevo_leon = Leon()


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))

    def __iter__(self):
        yield from self.cells


class TicTacToe(Board):
    def __init__(self):
        super().__init__(width=3, height=3)


class Song:
    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length

    def __int__(self):
        return self.length

    def __eq__(self, other):
        return int(self) == other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) > other or int(self) == other

    def __le__(self, other):
        return int(self) < other or int(self) == other


class Car:
    pass


class Van:
    pass


class Motorcycle:
    pass


def vehicle_factory(cls, count):
    for _ in range(count):
        yield cls()


cars = vehicle_factory(Car, 50)
vans = vehicle_factory(Van, 10)
motorcycles = vehicle_factory(Motorcycle, 100)


#******************************************************
import random


class Die:
    def __init__(self, sides=2):
        if sides < 2:
            raise ValueError("Can't have fewer than two sides")
        self.sides = sides
        self.value = random.randint(1, sides)

    def __int__(self):
        return self.value

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return self + other


class D20(Die):
    def __init__(self, sides=20, *args, **kwargs):
        super().__init__(sides)



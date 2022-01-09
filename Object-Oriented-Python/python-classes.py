class Student:

    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

    def praise(self):
        return "You inspire me, {}".format(self.name)

    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)

    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        return self.reassurance()


me = Student('Raul', midle='Alejandro')
print(me.feedback(grade=51))


class RaceCar:

    def __init__(self, color: str, fuel_remaining: int, **kwargs):
        self.laps: int = 0
        self.color = color
        self.fuel_remaining = fuel_remaining

        for key, value in kwargs.items():
            setattr(self, key, value)

    def run_lap(self, length: int):
        self.laps += 1
        self.fuel_remaining -= length * 0.125
        return self.fuel_remaining


tesla = RaceCar(color='Red', fuel_remaining=100)
print(tesla.run_lap(length=760))
print(tesla.laps)


class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)


class SortedInventory(Inventory):

    def add_item(self, *args):
        super().add_item(args)
        self.slots.sort()


supermarket = SortedInventory()
supermarket.add_item('Toronja', 'Guineo', 'Aguacate', 'Zapote', 'Banana')
print(supermarket.slots.sort())


class DreamCar:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return "My dream car is a {} {}.".format(self.make, self.model)


carro = DreamCar('Honda', 'Accord')
print(carro)


class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value

    def __mul__(self, other):
        if '.' in self.value:
            return float(self) * other
        return int(self) * other

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.value = self * other
        return self.value


class Inventory:
    def __init__(self):
        self.slots = []

    def add(self, item):
        self.slots.append(item)

    def __len__(self):
        return len(self.slots)

    def __contains__(self, item):
        return item in self.slots

    def __iter__(self):
        yield from self.slots


weapons = ['Pistol', "Grenade", 'Sword', 'Machete']
armas = Inventory()
armas.add(weapons)
for item in armas:
    print(armas.slots, sep='')


class Album:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __iter__(self):
        for song in self.songs:
            yield song


class ReversedStr(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self


rs = ReversedStr('Raul Alejandro Giron Jimenez')
print(rs)
print(len(rs))


class Double(int):
    def __new__(*args, **kwargs):
        self = int.__new__(*args, **kwargs)
        self = self * 2
        return self


class Liar(list):
    def __len__(self):
        return super().__len__() + 2

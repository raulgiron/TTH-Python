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

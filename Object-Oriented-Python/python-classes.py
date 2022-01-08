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

    def __init__(self, color, fuel_remaining, **kwargs):
        self.laps = 0
        self.color = color
        self.fuel_remaining = fuel_remaining

        for key, value in kwargs.items():
            setattr(self, key, value)

    def run_lap(self, length):
        self.laps += 1
        self.fuel_remaining -= length * 0.125
        return self.fuel_remaining

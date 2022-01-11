from dice import D20


class Hand(list):
    @property
    def total(self):
        return sum(self)

    def __init__(self,size=0, die_type= D20):
        super().__init__()
        for _ in range(size):
            self.append(die_type())

    @classmethod
    def roll(cls, size):
        return cls(size, die_type=D20)

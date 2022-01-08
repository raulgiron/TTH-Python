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

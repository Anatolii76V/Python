from animals.animal import Animal


class Mammal(Animal):
    def __init__(self, name, diet):
        super().__init__(name)
        self.diet = diet

    def info(self):
        return f"{self.name} - млекопитающее, питается {self.diet}."

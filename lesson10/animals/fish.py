from animals.animal import Animal


class Fish(Animal):
    def __init__(self, name, habitat):
        super().__init__(name)
        self.habitat = habitat

    def info(self):
        return f"{self.name} - рыба, обитает в {self.habitat}."

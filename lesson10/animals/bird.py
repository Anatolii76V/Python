from animals.animal import Animal


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def info(self):
        return f"{self.name} - птица, размах крыльев {self.wingspan} см."

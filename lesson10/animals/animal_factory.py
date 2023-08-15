from animals.fish import Fish
from animals.bird import Bird
from animals.mammal import Mammal


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        animal_types = {
            "Fish": Fish,
            "Bird": Bird,
            "Mammal": Mammal
        }
        if animal_type in animal_types:
            return animal_types[animal_type](*args)
        else:
            raise ValueError("Invalid animal type")

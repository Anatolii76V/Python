import sys

sys.path.append("/home/pc/PycharmProjects/lesson10/venv")

from animals.animal_factory import AnimalFactory

# Используем класс-фабрику для создания экземпляров
nemo = AnimalFactory.create_animal("Fish", "Немо", "океан")
robin = AnimalFactory.create_animal("Bird", "Робин", 30)
tiger = AnimalFactory.create_animal("Mammal", "Тигр", "мясом")

# Вывод информации
print(nemo.info())
print(robin.info())
print(tiger.info())

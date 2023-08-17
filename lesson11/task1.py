import time


class MyString(str):
    """
    Класс МояСтрока расширяет функциональность встроенного типа str,
    добавляя хранение имени автора и времени создания строки.

    Атрибуты:
        author (str): Имя автора строки.
        creation_time (float): Время создания строки в формате времени Unix.

    Пример использования:
        author_name = "Вася"
        my_string = МояСтрока("Привет, мир!", author=author_name)
        print(my_string)
    """

    def __new__(cls, value, author=None):
        instance = super().__new__(cls, value)
        instance.creation_time = time.time()
        instance.author = author
        return instance

    def __init__(self, value, author=None):
        super().__init__()

    def __str__(self):
        return super().__str__() + f"\nАвтор: {self.author}\nВремя создания: {self.creation_time}"


class Archive:
    """
    Класс Архив предоставляет возможность хранения числа и строки,
    а также сохранение старых данных в виде пары списков.

    Атрибуты:
        число_архив (list): Список для хранения чисел.
        строка_архив (list): Список для хранения строк.

    Методы:
        добавить(число, строка): Добавляет число и строку в архивы.
        получить_числа(): Возвращает список хранимых чисел.
        получить_строки(): Возвращает список хранимых строк.
        представление_программиста(): Возвращает представление архива для программиста.
        представление_пользователя(): Возвращает представление архива для пользователя.

    Пример использования:
        архив = Архив(42, "Пример")
        архив.добавить(123, "Дополнительный")
        архив.добавить(987, "Данные")
        print(архив.представление_программиста())
        print(архив.представление_пользователя())
    """

    def __init__(self, number, string):
        self.number_archive = []
        self.string_archive = []
        self.add(number, string)

    def add(self, number, string):
        self.number_archive.append(number)
        self.string_archive.append(string)

    def get_numbers(self):
        return self.number_archive

    def get_strings(self):
        return self.string_archive

    def programmer_representation(self):
        return f"Архив(число_архив={self.number_archive}, строка_архив={self.string_archive})"

    def user_representation(self):
        numbers = ', '.join(map(str, self.number_archive))
        strings = ', '.join(map(str, self.string_archive))
        return f"Числа: [{numbers}]\nСтроки: [{strings}]"


class Rectangle:
    """
        Класс Прямоугольник предоставляет функциональность для работы
        с прямоугольниками на плоскости.

        Атрибуты:
            длина (float): Длина прямоугольника.
            ширина (float): Ширина прямоугольника.

        Методы:
            площадь(): Возвращает площадь прямоугольника.
            периметр(): Возвращает периметр прямоугольника.
            __add__(other): Возвращает новый прямоугольник, полученный сложением периметров.
            __sub__(other): Возвращает новый прямоугольник, полученный вычитанием периметров.
            __eq__(other): Возвращает True, если площади прямоугольников равны.
            __lt__(other): Возвращает True, если площадь текущего прямоугольника меньше.
            __le__(other): Возвращает True, если площадь текущего прямоугольника меньше или равна.
            __gt__(other): Возвращает True, если площадь текущего прямоугольника больше.
            __ge__(other): Возвращает True, если площадь текущего прямоугольника больше или равна.

        Пример использования:
            прямоугольник1 = Прямоугольник(4, 5)
            прямоугольник2 = Прямоугольник(3, 6)
            прямоугольник3 = прямоугольник1 + прямоугольник2
            прямоугольник4 = прямоугольник3 - прямоугольник1
            if прямоугольник1 < прямоугольник2:
                print("Прямоугольник 1 меньше прямоугольника 2 по площади")
        """

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_length = self.perimeter() + other.perimeter()
            new_width = self.perimeter() + other.perimeter()
            return Rectangle(new_length, new_width)
        else:
            raise ValueError("Невозможно сложить с объектом другого типа")

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            new_length = max(self.perimeter() - other.perimeter(), 0)
            new_width = max(self.perimeter() - other.perimeter(), 0)
            return Rectangle(new_length, new_width)
        else:
            raise ValueError("Невозможно вычесть объект другого типа")

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            raise ValueError("Невозможно сравнить с объектом другого типа")

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.area() <= other.area()
        else:
            raise ValueError("Невозможно сравнить с объектом другого типа")

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        else:
            raise ValueError("Невозможно сравнить с объектом другого типа")

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.area() >= other.area()
        else:
            raise ValueError("Невозможно сравнить с объектом другого типа")


# Пример использования МояСтрока
author_name = "Вася"
my_string = MyString("Привет, мир!", author=author_name)
print(my_string)

# Пример использования Архив
archive = Archive(42, "Пример")
archive.add(123, "Дополнительный")
archive.add(987, "Данные")
print(archive.programmer_representation())
print(archive.user_representation())

# Пример использования Прямоугольник
rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(3, 6)
rectangle3 = rectangle1 + rectangle2
rectangle4 = rectangle3 - rectangle1
if rectangle1 < rectangle2:
    print("Прямоугольник 1 меньше прямоугольника 2 по площади")

import csv
import json
import math
import random


# Функция для нахождения корней квадратного уравнения
def solve_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root,
    else:
        return ()


# Функция для генерации CSV файла
def generate_csv(filename, rows):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for _ in range(rows):
            row = [random.random() for _ in range(3)]
            csv_writer.writerow(row)


# Декоратор для запуска функции нахождения корней квадратного уравнения с тройками чисел из CSV файла
def solve_quadratic_with_csv(func):
    def wrapper(filename):
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if len(row) == 3:
                    a, b, c = map(float, row)
                    roots = func(a, b, c)
                    print(f"Equation: {a}x^2 + {b}x + {c} = 0")
                    print("Roots:", roots)

    return wrapper


# Декоратор для сохранения параметров и результатов работы функции в JSON файл
def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                "args": args,
                "kwargs": kwargs,
                "result": result
            }
            with open(filename, 'w') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            return result

        return wrapper

    return decorator


# Пример использования
csv_filename = "random_numbers.csv"
json_filename = "results.json"

generate_csv(csv_filename, 1000)


@solve_quadratic_with_csv
def solve_quadratic_from_csv(a, b, c):
    return solve_quadratic(a, b, c)


@save_to_json(json_filename)
def solve_and_save(a, b, c):
    return solve_quadratic(a, b, c)


solve_quadratic_from_csv(csv_filename)
solve_and_save(1, 2, 1)

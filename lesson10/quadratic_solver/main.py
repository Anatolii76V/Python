import os
import sys

# Добавляем родительскую директорию в путь поиска
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solver import QuadraticSolver
from csv_generator import CSVGenerator
from decorators import solve_quadratic_with_csv, save_to_json

csv_filename = "random_numbers.csv"
json_filename = "results.json"

csv_generator = CSVGenerator()
csv_generator.generate_csv(csv_filename, 1000)


class MainApp:
    def __init__(self):
        self.quadratic_solver = QuadraticSolver()

    @solve_quadratic_with_csv
    def solve_quadratic_from_csv(self, a, b, c):
        return self.quadratic_solver.solve_quadratic(a, b, c)

    @save_to_json(json_filename)
    def solve_and_save(self, a, b, c):
        return self.quadratic_solver.solve_quadratic(a, b, c)


app = MainApp()
app.solve_quadratic_from_csv(csv_filename)
app.solve_and_save(1, 2, 1)

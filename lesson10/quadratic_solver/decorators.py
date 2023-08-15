import csv
import json


def solve_quadratic_with_csv(func):
    def wrapper(self, filename):
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if len(row) == 3:
                    a, b, c = map(float, row)
                    roots = func(self, a, b, c)
                    print(f"Equation: {a}x^2 + {b}x + {c} = 0")
                    print("Roots:", roots)

    return wrapper


def save_to_json(filename):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
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

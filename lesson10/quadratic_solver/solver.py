import math


class QuadraticSolver:
    def solve_quadratic(self, a, b, c):
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

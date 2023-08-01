import random


def random_queens_positions():
    queens_positions = []
    n = 8

    def is_safe(queens_positions, row, col):

        for r, c in queens_positions:
            if row == r or col == c or abs(row - r) == abs(col - c):
                return False
        return True

    def backtrack(row):
        if row == n:
            return True

        for col in range(n):
            if is_safe(queens_positions, row, col):
                queens_positions.append((row, col))
                if backtrack(row + 1):
                    return True
                queens_positions.pop()

        return False

    backtrack(0)

    return queens_positions


def main():
    successful_count = 0
    max_attempts = 10000
    for attempt in range(1, max_attempts + 1):
        queens_positions = random_queens_positions()

        def is_safe(row, col):

            for r, c in queens_positions:
                if row == r or col == c or abs(row - r) == abs(col - c):
                    return False
            return True

        valid_arrangement = all(not is_safe(queens_positions[i][0], queens_positions[i][1])
                                for i in range(len(queens_positions)))

        if valid_arrangement:
            successful_count += 1
            print_solution(queens_positions, successful_count)

        if successful_count == 4:
            break

    if successful_count < 4:
        print("Не удалось найти 4 успешные расстановки.")


def print_solution(queens_positions, successful_count):
    print(f"Расстановка {successful_count}: ", end="")
    for row, col in queens_positions:
        col_str = chr(ord('A') + col)
        print(f"{col_str}{row + 1}", end=" ")
    print()


if __name__ == "__main__":
    print("4 успешные расстановки ферзей:")
    main()

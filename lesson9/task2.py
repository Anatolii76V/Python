from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10


def guess_number():
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    attempts = 0
    print(num)

    while attempts < MAX_ATTEMPTS:
        guess = int(input("Угадайте число от 0 до 1000: "))
        attempts += 1

        if guess < num:
            print("Загаданное число больше.")
        elif guess > num:
            print("Загаданное число меньше.")
        else:
            print(f"Вы угадали число {num} за {attempts} попыток.")
            return

    print(f"Вы исчерпали все попытки. Загаданное число было {num}.")


def is_queen_attack(pos1, pos2):
    return pos1[0] == pos2[0] or pos1[1] == pos2[1] or abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


def check_queens_attack(queens_positions):
    for i in range(len(queens_positions)):
        for j in range(i + 1, len(queens_positions)):
            if is_queen_attack(queens_positions[i], queens_positions[j]):
                return False
    return True


if __name__ == "__main__":
    choice = input("Выберите игру: (1) - Угадай число, (2) - Ферзи: ")

    if choice == '1':
        guess_number()
    elif choice == '2':
        positions = [(1, 2), (3, 4), (5, 6)]  # Здесь можно указать позиции ферзей
        print(check_queens_attack(positions))
    else:
        print("Неверный выбор.")

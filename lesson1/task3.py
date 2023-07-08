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


guess_number()

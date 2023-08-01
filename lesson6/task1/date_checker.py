import sys
from datetime import datetime


def is_valid_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def main():
    if len(sys.argv) != 2:
        print("Usage: python date_checker.py <date>")
        return

    date_str = sys.argv[1]
    if is_valid_date(date_str):
        print(f"The date {date_str} is valid.")
    else:
        print(f"The date {date_str} is invalid. Please provide a date in the format YYYY-MM-DD.")


if __name__ == "__main__":
    main()

# python date_checker.py 2023-07-20   -В терминале в водим команду.

# Получаем результат:
# (venv) pc@pc-desktop:~/PycharmProjects/lesson6/venv$ python date_checker.py 2023-07-20
# The date 2023-07-20 is valid.

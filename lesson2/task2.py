import fractions
import math


def _fraction(fraction_str):
    numerator, _, denominator = fraction_str.partition("/")
    return fractions.Fraction(int(numerator), int(denominator))


def adding_fractions(a, b):
    return a + b


def multiplication_fractions(a, b):
    return a * b


def add_fractions(a_num, a_denom, b_num, b_denom):
    common_denom = a_denom * b_denom
    a_num *= b_denom
    b_num *= a_denom
    return a_num + b_num, common_denom


def multiply_fractions(a_num, a_denom, b_num, b_denom):
    return a_num * b_num, a_denom * b_denom


def simplify_fraction(num, denom):
    gcd_value = math.gcd(num, denom)
    return num // gcd_value, denom // gcd_value


# Получаем входные данные от пользователя
try:
    f1 = input("Введите первую дробь (вида a/b): ")
    f2 = input("Введите вторую дробь (вида a/b): ")

    fraction1 = _fraction(f1)
    fraction2 = _fraction(f2)

    num1, denom1 = fraction1.numerator, fraction1.denominator
    num2, denom2 = fraction2.numerator, fraction2.denominator

except ValueError:
    print("Ошибка: Введите допустимые дробные числа в формате a/b.")
else:
    # Выполняем арифметические операции с дробями, используя модуль fractions
    Sum_fractions = adding_fractions(fraction1, fraction2)
    product_fraction = multiplication_fractions(fraction1, fraction2)

    # Выполняем арифметические операции с числителями и знаменателями
    sum_num, sum_denom = add_fractions(num1, denom1, num2, denom2)
    product_num, product_denom = multiply_fractions(num1, denom1, num2, denom2)

    # Сокращаем результаты
    simplified_sum, simpl_sum_denom = simplify_fraction(sum_num, sum_denom)
    simplified_product, simplified_denom = simplify_fraction(product_num, product_denom)

    print("Результаты, используя модуль fractions:")
    print(f"Сумма дробей: {Sum_fractions}")
    print(f"Произведение дробей: {product_fraction}")

    print("\nРезультаты, используя арифметические операции:")
    print(f"Сумма дробей: {simplified_sum}/{simpl_sum_denom}")
    print(f"Произведение дробей: {simplified_product}/{simplified_denom}")

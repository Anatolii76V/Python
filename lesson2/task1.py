def decimal_to_hexadecimal(number):
    hex_digits = "0123456789abcdef"

    if number == 0:
        return "0"

    hex_representation = ""

    while number > 0:
        hex_representation = hex_digits[number % 16] + hex_representation
        number //= 16

    return "0x" + hex_representation


# Получение входного числа от пользователя
try:
    input_number = int(input("Введите целое число: "))
except ValueError:
    print("Ошибка: Введите целое число.")
else:
    # Получение шестнадцатеричного представления с помощью пользовательской функции
    hex_representation_custom = decimal_to_hexadecimal(input_number)

    # Получение шестнадцатеричного представления с помощью встроенной функции hex()
    hex_input_number = hex(input_number)

    print(f"Шестнадцатеричное представление числа {input_number}: {hex_representation_custom}")
    print(f"Преобразование используя функцию hex: {hex_input_number}")

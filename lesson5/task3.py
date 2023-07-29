def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Пример использования функции для получения первых 20 чисел Фибоначчи
fibonacci_gen = fibonacci_generator()
fibonacci_sequence = [next(fibonacci_gen) for _ in range(20)]
print(fibonacci_sequence)

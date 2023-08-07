# Вариант 2
import os


def group_rename_files(desired_name, digits_count, source_extension, destination_extension, range_start, range_end):
    # Получение списка файлов в текущем каталоге
    files = os.listdir()

    # Фильтрация файлов по расширению исходного файла
    source_files = [file for file in files if file.endswith(source_extension)]

    # Проверка наличия файлов для переименования
    if len(source_files) == 0:
        print("No files found for renaming.")
        return

    # Проход по каждому файлу для переименования
    for i, filename in enumerate(sorted(source_files)):
        # Генерация порядкового номера с заданным количеством цифр
        counter = str(i + 1).zfill(digits_count)

        # Получение диапазона сохраняемого оригинального имени
        original_name_range = filename[range_start - 1:range_end]

        # Формирование нового имени файла
        new_filename = original_name_range + desired_name + counter + '.' + destination_extension

        # Переименование файла
        os.rename(filename, new_filename)

        # Вывод информации о переименовании
        print(f"Renamed '{filename}' to '{new_filename}'.")


# Пример использования функции
group_rename_files("new_name_", 3, ".txt", "dat", 3, 6)

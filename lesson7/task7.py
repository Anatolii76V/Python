# функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
import os
import shutil


def sort_files_by_type(source_dir, destination_dir):
    extensions = {
        'Видео': ['.mp4', '.avi', '.mkv'],
        'Изображения': ['.jpg', '.jpeg', '.png', '.gif'],
        'Текст': ['.txt', '.doc', '.docx'],
        # Добавьте другие типы файлов и соответствующие расширения по необходимости
    }

    # Создание директорий в папке назначения
    for directory in extensions.keys():
        os.makedirs(os.path.join(destination_dir, directory), exist_ok=True)

    # Перебор файлов в исходной папке
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isfile(file_path):
            # Определение расширения файла
            _, extension = os.path.splitext(filename)

            # Поиск соответствующей директории для файла
            for directory, ext_list in extensions.items():
                if extension.lower() in ext_list:
                    dest_dir = os.path.join(destination_dir, directory)
                    try:
                        # Используем операцию копирования и удаления исходного файла
                        shutil.copy(file_path, dest_dir)
                        os.remove(file_path)
                    except Exception as e:
                        print(f"Ошибка при обработке файла {filename}: {e}")
                    break


# Пример использования
source_directory = '/home/pc/Documents'

destination_directory = '/home/pc/Documents/destination'

sort_files_by_type(source_directory, destination_directory)

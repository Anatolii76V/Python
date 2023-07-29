import os


def split_file(file_path):
    # Разделяем путь и имя файла
    file_dir, file_name = os.path.split(file_path)

    # Разделяем имя файла и его расширение
    file_name, file_extension = os.path.splitext(file_name)

    return file_dir, file_name, file_extension


file_path = "/home/pc/PycharmProjects/lesson5/task1.py"
result = split_file(file_path)
print(result)

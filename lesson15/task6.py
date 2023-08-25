# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
#
# ○имя файла без расширения или название каталога,
# ○расширение, если это файл,
# ○флаг каталога,
# ○название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.


from collections import namedtuple
import logging
import argparse
from pathlib import Path

logging.basicConfig(filename='task6.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

File = namedtuple('File', 'name, extension, is_dir, parent_dir')


def read_dir(path: Path):
    for file in path.iterdir():
        is_dir = file.is_dir()
        f = File(file.stem if not is_dir else file.name,
                 file.suffix if not is_dir else '',
                 is_dir,
                 file.parent.name if is_dir else file.parent)
        logger.info(f)
        if is_dir:
            read_dir(file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Обработать путь к директории.')
    parser.add_argument('directory', type=str, help='Путь к обрабатываемой директории')
    args = parser.parse_args()

    directory_path = Path(args.directory)
    if directory_path.exists() and directory_path.is_dir():
        read_dir(directory_path)
    else:
        print(f"Путь к каталогу для обработки '{directory_path}' не существует или не является каталогом.")

# Запускаю командой в терминале: sudo /home/pc/PycharmProjects/lesson15/venv/bin/python
# /home/pc/PycharmProjects/lesson15/venv/task6.py /home/pc/documents

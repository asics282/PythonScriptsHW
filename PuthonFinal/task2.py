import os
import logging
from collections import namedtuple
import argparse

logging.basicConfig(filename='log.log',
                    level=logging.INFO,
                    format='[{levelname:<8}] {asctime}: {msg}',
                    style='{')

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def d_info(directory_path):
    try:
        if not os.path.isdir(directory_path):
            raise ValueError(f"Указанный путь не является допустимым каталогом: {directory_path}")

        with open('log.log', 'w') as log_file:
            log_file.write("Сбор информации о директории...\n")

            for item in os.listdir(directory_path):
                item_path = os.path.join(directory_path, item)

                is_directory = os.path.isdir(item_path)
                parent_directory = os.path.basename(directory_path)

                if is_directory:
                    file_info = FileInfo(name=item, extension="", is_directory=is_directory, parent_directory=parent_directory)
                else:
                    name, extension = os.path.splitext(item)
                    file_info = FileInfo(name=name, extension=extension, is_directory=is_directory, parent_directory=parent_directory)

                log_file.write(f"{file_info}\n")
                logging.info(f"Собранная информация: {file_info}")

    except Exception as e:
        logging.error(f"Ошибка: {str(e)}")


def main():
    parser = argparse.ArgumentParser(description="Сбор информации о содержимом каталога.")
    parser.add_argument('directory_path', type=str, help='Путь к директории на компьютере.')

    args = parser.parse_args()

    d_info(args.directory_path)


if __name__ == "__main__":
    main()

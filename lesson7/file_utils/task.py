import random
import string
import os
import shutil


def fill_file_with_random_pairs(filename, num_lines):
    pass


def generate_pseudo_names(filename, num_names):
    pass


def multiply_numbers_and_save(input_filename_numbers, input_filename_names, output_filename):
    pass


def create_files_with_extension(extension, min_name_length=6, max_name_length=30, min_bytes=256, max_bytes=4096,
                                num_files=42):
    pass


def generate_files_with_extensions(extensions, num_files_per_extension, *args, **kwargs):
    pass


def generate_files_in_directory(directory, *args, **kwargs):
    pass


def sort_files_by_type(source_dir, destination_dir):
    pass


if __name__ == "__main__":
    fill_file_with_random_pairs("numbers.txt", 10)
    generate_pseudo_names("names.txt", 5)
    multiply_numbers_and_save("numbers.txt", "names.txt", "result.txt")

    create_files_with_extension("txt")
    generate_files_with_extensions(["mp3", "pdf"], 3)
    generate_files_in_directory("files_directory", "txt", 5, 10, 1024, 2048, 3)

    source_directory = '/home/pc/Documents'
    destination_directory = '/home/pc/Documents/destination'
    sort_files_by_type(source_directory, destination_directory)

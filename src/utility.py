import os
from src.constants import IO_PATH


def load_file_commands(filename):
    file_path = os.path.join(os.getcwd(), IO_PATH, filename)
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def write_to_file(filename, data):
    file_path = os.path.join(os.getcwd(), IO_PATH, filename)
    with open(file_path, 'w') as file:
        file.write(data)


def print_wrapper(text):
    print('OUTPUT:\n{0}'.format(text))

import os


def load_file_commands(filename):
    if not os.path.exists(filename):
        print_wrapper('File does not exists at\n{0}'.format(filename))
    with open(filename, 'r') as file:
        return file.read().splitlines()


def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)


def print_wrapper(text):
    print('OUTPUT:\n{0}'.format(text))

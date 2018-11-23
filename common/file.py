import os

__location__ = os.path.realpath(os.path.join(os.getcwd()))


def __get_path(path, filename):
    return os.path.join(os.path.dirname(path), filename)


def read_file(path, filename):
    file = open(__get_path(path, filename), 'r')
    content = file.read()
    file.close()
    return content


def read_file_lines(path, filename):
    return read_file(path, filename).splitlines()


def write_file(path, filename, output):
    file = open(__get_path(path, filename), 'w')
    file.write(output)
    file.close()


def write_file_lines(path, filename, lines):
    file = open(__get_path(path, filename), 'w')
    file.write('\n'.join(lines) + '\n')
    file.close()


def delete_file(path, filename):
    path = __get_path(path, filename)
    if os.path.isfile(path):
        os.remove(path)
    else:
        print("Error: %s file not found" % path)

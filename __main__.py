from commands.core import read_command
from matrix_io.matrix_printer import print_matrix


def main():
    result = None

    while type(result) != str:
        result = read_command()

        if result is not None:
            print_matrix(result)


if __name__ == "__main__":
    main()

import gnureadline
import sympy
from commands.core import read_command


def main():
    result = None

    while type(result) != str:
        result = read_command()

        if result is not None:
            sympy.pprint(result)
            print()


if __name__ == "__main__":
    main()

from numpy import array, insert
from fractions import Fraction

end_command = "END"


def read_matrix():
    print("Enter a new matrix:")
    data = ""
    matrix = []

    number_of_columns = 0

    while data.upper() != end_command:
        data = input()
        if data.upper() != end_command:
            try:
                row = data.split(" ")
                fraction_row = list(map(Fraction, row))

                if number_of_columns == 0:
                    number_of_columns = len(fraction_row)
                    matrix.append(fraction_row)
                elif number_of_columns != len(fraction_row):
                    print(
                        "Invalid input. The matrix must have the same number of columns in each row. Please try again:"
                    )
                else:
                    matrix.append(fraction_row)

            except ValueError:
                print("Invalid input. Please try again:")
                matrix = []

    if len(matrix) == 0:
        print("No matrix was read")
    else:
        matrix = array(matrix)

    return matrix

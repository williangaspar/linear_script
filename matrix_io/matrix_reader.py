from sympy import Matrix
from fractions import Fraction

end_command = "D"


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
                is_end_line = False
                if row[len(row) - 1].upper() == end_command:
                    is_end_line = True
                    row = row[:-1]
                
                fraction_row = list(map(Fraction, row))

                if number_of_columns == 0:
                    number_of_columns = len(fraction_row)
                    matrix.append(fraction_row)
                    if is_end_line:
                        break
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
        matrix = Matrix(matrix)

    return matrix

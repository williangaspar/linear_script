def pad_number(number, pad):
    pad_length = pad - len(str(number))
    return " " * pad_length + str(number)


def get_matrix_pad(matrix):
    max_padding = 0
    for row in matrix:
        for number in row:
            len_number = len(str(number))
            if len_number > max_padding:
                max_padding = len_number
    return max_padding


def print_matrix(matrix, is_augmented=False):
    rows, columns = matrix.shape
    pad = get_matrix_pad(matrix)

    for row in range(rows):
        current_row = matrix[row]
        string_row = "| "
        for column in range(columns):
            if column == columns - 1 and is_augmented:
                string_row += ":"
            string_row += pad_number(current_row[column], pad) + " "
        string_row += "|"
        print(string_row)


def print_augumented_matrix(matrix):
    print_matrix(matrix, True)

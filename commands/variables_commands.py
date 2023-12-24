import sympy
import json
import os

from commands.variables import get_variable, is_valid_variable_name, set_variable
from matrix_io.matrix_reader import read_matrix

REAL_PATH = os.path.dirname(os.path.dirname(__file__))
VARAIBLE_JSON_FILE = os.path.join(REAL_PATH, "variables.data")


def read_variable(params):
    variable_name = params[0]

    is_valid = is_valid_variable_name(variable_name)

    if not is_valid:
        return None, "Invalid variable name: " + variable_name

    value = read_matrix()
    success = set_variable(variable_name, value)

    if not success:
        return None, "Could not read variable " + variable_name

    return value, None


def print_value(params):
    param = params[0]

    # Print a matrix object
    if isinstance(param, sympy.Matrix):
        sympy.pprint(param)
        return None, None

    # Print a variable
    variable = get_variable(param)

    if variable is None:
        return None, "Variable '" + param + "' is not defined."
    else:
        sympy.pprint(variable.value)
        print()

    return None, None


def set_variable_command(params):
    variable_name = params[0]
    variable_value = params[1]

    is_name_valid = is_valid_variable_name(variable_name)

    if not is_name_valid:
        return None, "Invalid variable name: " + variable_name

    is_value_a_variable = isinstance(variable_value, str)

    if is_value_a_variable:
        variable = get_variable(variable_value)

        if variable is None:
            return None, "Variable '" + variable_value + "' is not defined."

        variable_value = variable.value

    success = set_variable(variable_name, variable_value)

    if success:
        return variable_value, None

    else:
        return None, "Could not set variable " + variable_name


def append_or_replace_to_file(file_name, variable_name, variable_value):
    f = open(file_name, "r")
    lines = f.readlines()
    f.close()

    f = open(file_name, "w")

    for line in lines:
        if variable_name not in line:
            f.write(line)

    f.write(variable_name + str(variable_value).replace("'", '"') + "\n")
    f.close()


def stringfyMatrix(matrix):
    col, row = matrix.shape
    new_matrix = []
    for i in range(col):
        for j in range(row):
            new_row = []
            new_row.append(str(matrix[i, j]))
        new_matrix.append(new_row)
    return new_matrix


def store_variable(params):
    variable_name = params[0]

    is_valid = is_valid_variable_name(variable_name)

    if not is_valid:
        return None, "Invalid variable name: " + variable_name

    variable = get_variable(variable_name)

    if variable is None:
        return None, "Variable '" + variable_name + "' is not defined."

    append_or_replace_to_file(
        VARAIBLE_JSON_FILE, variable_name, stringfyMatrix(variable.value)
    )

    return None, None


def load_variable(params):
    variable_name = params[0]

    is_valid = is_valid_variable_name(variable_name)

    if not is_valid:
        return None, "Invalid variable name: " + variable_name

    f = open(VARAIBLE_JSON_FILE, "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        if line[0] == variable_name:
            value = json.loads(line[1:])
            value = sympy.Matrix(value)
            set_variable(variable_name, value)
            return value, None

    return None, "Could not load variable " + variable_name

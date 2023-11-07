from commands.variables import get_variable, set_variable
from matrix_io.matrix_printer import print_matrix
from matrix_io.matrix_reader import read_matrix


def read_variable(params):
    var_name = params[0]
    value = read_matrix()
    success = set_variable(var_name, value)
    if not success:
        return None, "Invalid variable name: " + var_name

    return value, None


def print_value(params):
    param = params[0]

    if type(param) is not str:
        print_matrix(param)
        return

    variable = get_variable(param)

    if variable is None:
        return None, "Variable '" + param + "' is not defined."
    else:
        print_matrix(variable.value)

    return None, None


def set_variable_command(params):
    pass


def get_variable_command():
    pass


def store_variable():
    pass


def load_variable():
    pass

import sympy as sp
from commands.variables import Variable, get_variable


def det(params):
    variable_name = params[0]

    variable = get_variable(variable_name)

    if variable is None:
        return None, "Variable '" + variable_name + "' is not defined."

    if variable.value.shape[0] != variable.value.shape[1]:
        return None, "det requires a square matrix."

    matrix = sp.Matrix(variable.value)

    return matrix.det(), None


def rref(params):
    variable_name = params[0]

    variable = get_variable(variable_name)

    if variable is None:
        return None, "Variable '" + variable_name + "' is not defined."

    matrix = sp.Matrix(variable.value)
    return matrix.rref()[0], None


def valida_variable(params):
    variables = []
    for param in params:
        variable_name = param

        is_str_variable = isinstance(variable_name, str)

        if not is_str_variable:
            variables.append(Variable("@", param))
            continue

        variable = get_variable(variable_name)

        if variable is None:
            return None, "Variable '" + variable_name + "' is not defined."
        else:
            variables.append(variable)

    return variables, None


def dot(params):
    variables, Error = valida_variable(params)

    if Error is not None:
        return None, Error

    return variables[0].value @ variables[1].value, None


def inv(params):
    variables, Error = valida_variable(params)

    if Error is not None:
        return None, Error

    if len(variables) == 1:
        return variables[0].value.inv(), None

    return None, "Could not invert matrix."


def transp(params):
    variables, Error = valida_variable(params)

    if Error is not None:
        return None, Error

    return variables[0].value.T, None


def solve():
    pass

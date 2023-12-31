import sympy as sp
from commands.variables import Variable, get_variable


def det(params):
    variables, Error = valida_variable(params)

    if Error is not None:
        return None, Error

    if len(variables) == 0:
        return None, "Variable '" + params[0] + "' is not defined."

    variable = variables[0]

    if variable.value.shape[0] != variable.value.shape[1]:
        return None, "det requires a square matrix."

    matrix = sp.Matrix(variable.value)

    return matrix.det(), None


def rref(params):
    variables, Error = valida_variable(params)

    if Error is not None:
        return None, Error

    if len(variables) == 0:
        return None, "Variable '" + params[0] + "' is not defined."

    variable = variables[0]

    matrix = sp.Matrix(variable.value)
    return matrix.rref()[0], None


def dot(params):
    variables, Error = valida_variable(params)

    if Error is not None:
        return None, Error

    _, col_var_1 = variables[0].value.shape
    _, col_var_2 = variables[1].value.shape

    if col_var_1 == 1 and col_var_2 == 1:
        return variables[0].value.dot(variables[1].value), None

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


def eigVal(params):
    variables, Error = valida_variable(params)

    if Error is not None:
        return None, Error

    elgVals = variables[0].value.eigenvals()

    elgVal_result = []

    for eigVal in elgVals:
        elgVal_result.append(eigVal)

    return sp.Matrix(elgVal_result), None


def solve():
    pass


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

def add(params):
    variables, Error = valida_variable(params)

    if Error is not None:
        return None, Error

    if len(variables) == 2:
        return variables[0].value + variables[1].value, None

    return None, "Could not add matrix."
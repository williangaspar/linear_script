import sympy as sp
from commands.variables import Variable, get_variable
from commands.tokens import is_numeric, get_numeric_value


def det(params):
    variables, Error = validate_variable(params)

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
    variables, Error = validate_variable(params)

    if Error is not None:
        return None, Error

    if len(variables) == 0:
        return None, "Variable '" + params[0] + "' is not defined."

    variable = variables[0]

    matrix = sp.Matrix(variable.value)
    return matrix.rref()[0], None


def dot(params):
    variables, Error = validate_variable(params)

    if Error is not None:
        return None, Error

    _, col_var_1 = variables[0].value.shape
    _, col_var_2 = variables[1].value.shape

    if col_var_1 == 1 and col_var_2 == 1:
        return variables[0].value.dot(variables[1].value), None

    return variables[0].value @ variables[1].value, None


def inv(params):
    variables, Error = validate_variable(params)

    if Error is not None:
        return None, Error

    if len(variables) == 1:
        return variables[0].value.inv(), None

    return None, "Could not invert matrix."


def transp(params):
    variables, Error = validate_variable(params)

    if Error is not None:
        return None, Error

    return variables[0].value.T, None


def eigVal(params):
    variables, Error = validate_variable(params)

    if Error is not None:
        return None, Error

    elgVals = variables[0].value.eigenvals()

    elgVal_result = []

    for eigVal in elgVals:
        elgVal_result.append(eigVal)

    return sp.Matrix(elgVal_result), None


def solve():
    pass


def validate_variable(params):
    variables = []
    for param in params:
        variable_name = param

        is_str_variable = isinstance(variable_name, str)

        if not is_str_variable:
            variables.append(Variable("@", param))
            continue

        # Check if the parameter is a numeric value
        if is_numeric(variable_name):
            numeric_value = get_numeric_value(variable_name)
            variables.append(Variable("@numeric", numeric_value))
            continue

        variable = get_variable(variable_name)

        if variable is None:
            return None, "Variable '" + variable_name + "' is not defined."
        else:
            variables.append(variable)

    return variables, None

def add(params):
    variables, Error = validate_variable(params)

    if Error is not None:
        return None, Error

    if len(variables) == 2:
        return variables[0].value + variables[1].value, None

    return None, "Could not add matrix."

def sub(params):
    variables, Error = validate_variable(params)

    if Error is not None:
        return None, Error

    if len(variables) == 2:
        return variables[0].value - variables[1].value, None

    return None, "Could not subtract matrix."

def mult(params):
    variables, Error = validate_variable(params)

    if Error is not None:
        return None, Error

    if len(variables) == 2:
        var1, var2 = variables[0], variables[1]
        
        # Check if either variable is a scalar (numeric value)
        var1_is_scalar = var1.name == "@numeric" or (hasattr(var1.value, 'shape') and var1.value.shape == (1, 1))
        var2_is_scalar = var2.name == "@numeric" or (hasattr(var2.value, 'shape') and var2.value.shape == (1, 1))
        
        # Scalar multiplication: scalar * matrix or matrix * scalar
        if var1_is_scalar and not var2_is_scalar:
            # scalar * matrix
            scalar = var1.value if var1.name == "@numeric" else var1.value[0, 0]
            return scalar * var2.value, None
        elif var2_is_scalar and not var1_is_scalar:
            # matrix * scalar
            scalar = var2.value if var2.name == "@numeric" else var2.value[0, 0]
            return var1.value * scalar, None
        else:
            # Matrix multiplication or scalar * scalar
            return var1.value * var2.value, None

    return None, "Could not multiply matrix."

def cross(params):
    variables, Error = validate_variable(params)

    if Error is not None:
        return None, Error

    if len(variables) == 2:
        return variables[0].value.cross(variables[1].value), None

    return None, "Could not cross product matrix."

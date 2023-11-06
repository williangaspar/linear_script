class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.det = None


variable_list = []


def is_valid_variable_name(name):
    size = len(name)
    if size == 0:
        return False
    if not name[0].isalpha():
        return False
    if size > 1:
        return False
    return True


def get_variable_index(name):
    for i in range(len(variable_list)):
        if variable_list[i].name == name:
            return i
    return -1


def set_variable(name, value):
    if is_valid_variable_name(name):
        index = get_variable_index(name)
        if index != -1:
            variable_list[index].value = value
            variable_list[index].det = None
        else:
            variable_list.append(Variable(name, value))
        return True
    return False


def get_variable(name):
    for variable in variable_list:
        if variable.name == name:
            return variable
    return None

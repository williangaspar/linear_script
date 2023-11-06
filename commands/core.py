from commands.tokens import TokenItem, get_tokens
from commands.variables import is_valid_variable_name
from .command_list import command_list


def is_valid_command(command):
    for cmd in command_list:
        if cmd.name == command:
            return True, cmd
    return False, None


def read_command():
    command = input(">> ")
    tokens = get_tokens(command)
    is_valid, error = validate_input(tokens)

    if is_valid:
        execute_command(tokens)
    else:
        print(error)


def pop_element_from_stack(command_token_list):
    if len(command_token_list) > 0:
        top_cmd = command_token_list[-1]
        if len(top_cmd.param_list) == top_cmd.num_params:
            name = top_cmd.token
            command_token_list.pop()

            if len(command_token_list) > 0:
                top_cmd = command_token_list[-1]
                top_cmd.param_list.append(name)

    return command_token_list


def validate_input(tokens):
    command_token_list = []

    if len(tokens) == 0:
        return True, None

    for token in tokens:
        is_valid_cmd, cmd = is_valid_command(token)
        if is_valid_cmd:
            command_token_list = pop_element_from_stack(command_token_list)
            command_token_list.append(TokenItem(token, True, cmd.num_params))
        elif is_valid_variable_name(token):
            top_cmd = command_token_list[-1]

            if len(top_cmd.param_list) == top_cmd.num_params:
                return False, "Too many parameters for command: " + top_cmd.token

            top_cmd.param_list.append(token)

        else:
            return False, "Invalid token: " + token

    # Clear stack
    len_command_token_list = len(command_token_list)

    counter = 0

    while counter < len_command_token_list and len(command_token_list):
        counter = counter + 1
        command_token_list = pop_element_from_stack(command_token_list)

    # If there still any elements in the list there is probably an error
    for token in command_token_list:
        if token.num_params > len(token.param_list):
            return False, "Too few parameters for command: " + token.token

    return True, None


def execute_command(tokens):
    pass

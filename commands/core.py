from commands.tokens import SyntaxToken, TokenItem, get_tokens
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
    is_valid, error = validate_input(tokens.copy())

    if is_valid:
        return execute_commands(tokens)
    else:
        print(error)
        return None


MAX_STACK_DEPTH = 16


def validate_input(tokens):
    if len(tokens) == 0:
        return True, None

    root_token = tokens.pop(0)

    is_valid_cmd, cmd = is_valid_command(root_token)

    max_depth = 0

    if is_valid_cmd:
        root = SyntaxToken(root_token, True, cmd.num_params)

        try:
            for _ in range(root.num_params):
                token = make_tree(tokens, root, max_depth)

                if token is not None:
                    is_valid_cmd, cmd = is_valid_command(token)

                    if not is_valid_cmd:
                        root.param_list.append(token)

            if len(root.param_list) < root.num_params:
                return False, "Not enough parameters for command: " + root_token

            if len(tokens) > 0:
                return False, "Too many parameters for command: " + root_token

        except Exception as e:
            return False, str(e)

        return True, None
    else:
        return False, root_token + " is not a valid command"


def make_tree(tokens, root, max_depth):
    if max_depth > MAX_STACK_DEPTH:
        raise Exception("Stack overflow")

    max_depth = max_depth + 1

    if len(tokens) == 0:
        return None

    token = tokens.pop(0)

    is_valid_cmd, cmd = is_valid_command(token)

    if is_valid_cmd:
        if cmd.is_void:
            raise Exception(
                token + " is a void command and cannot be used as a parameter",
            )

        sintax_token = SyntaxToken(token, True, cmd.num_params)
        sintax_token.cmd = cmd
        root.param_list.append(sintax_token)

        for _ in range(sintax_token.num_params):
            value = make_tree(tokens, sintax_token, max_depth)

            if value is None:
                raise Exception("Not enough parameters for command: " + root.token)

            sintax_token.param_list.append(value)

        return sintax_token.token
    elif is_valid_variable_name(token):
        return token
    else:
        raise Exception("Invalid token: " + token)


def execute_commands(tokens):
    if len(tokens) == 0:
        return None

    stack = []
    max_depth = 0
    return execute_command_stack(stack, tokens, max_depth)


def execute_command_stack(stack, tokens, max_depth):
    max_depth = max_depth + 1

    if max_depth > MAX_STACK_DEPTH:
        raise Exception("Stack overflow")

    token = tokens.pop(0)

    is_valid_cmd, cmd = is_valid_command(token)

    if is_valid_cmd:
        token_item = TokenItem(token, True, cmd.num_params)
        token_item.cmd = cmd
        stack.append(token_item)
    elif is_valid_variable_name(token):
        return token

    if len(stack) > 0:
        root_cmd = stack[-1]

        for _ in range(root_cmd.num_params):
            param = execute_command_stack(stack, tokens, max_depth)

            if param is None:
                print("Not enough parameters for command: " + root_cmd.token)
                return None

            root_cmd.param_list.append(param)

        try:
            value, error = root_cmd.cmd.execute(root_cmd.param_list)

            if error is not None:
                print(error)
                return None
        except Exception as e:
            print(e)
            return None

        stack.pop()

    return value

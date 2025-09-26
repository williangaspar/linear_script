class TokenItem:
    def __init__(self, token, is_cmd, num_params=0):
        self.token = token
        self.is_cmd = is_cmd
        self.num_params = num_params
        self.param_list = []
        self.cmd = None


class SyntaxToken:
    def __init__(self, token, is_cmd, num_params=0):
        self.token = token
        self.is_cmd = is_cmd
        self.num_params = num_params
        self.param_list = []
        self.parent = None


def is_numeric(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


def get_numeric_value(token):
    try:
        # Try to convert to int first, then float
        if '.' in token:
            return float(token)
        else:
            return int(token)
    except ValueError:
        return None


def get_tokens(command):
    # Brackets and parenthesis are allowed but do not count as tokens.
    # They serve as a guide to the user.
    command = command.replace("[", "")
    command = command.replace("]", "")
    command = command.replace("(", "")
    command = command.replace(")", "")

    tokens = command.split()

    return tokens

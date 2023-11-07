class TokenItem:
    def __init__(self, token, is_cmd, num_params=0):
        self.token = token
        self.is_cmd = is_cmd
        self.num_params = num_params
        self.param_list = []
        self.cmd = None


def get_tokens(command):
    # Brackets and parenthesis are allowed but do not count as tokens.
    # They serve as a guide to the user.
    command = command.replace("[", "")
    command = command.replace("]", "")
    command = command.replace("(", "")
    command = command.replace(")", "")

    tokens = command.split()

    return tokens

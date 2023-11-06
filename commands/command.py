class Command:
    def __init__(self, name, description, num_params, function, is_void=False):
        self.name = name
        self.description = description
        self.function = function
        self.num_params = num_params
        self.is_void = is_void

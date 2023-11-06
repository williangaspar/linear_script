from commands.command import Command

command_list = []

command_list.append(Command("rref", "Row reduce a matrix. Ex: rref A", 1, None))
command_list.append(
    Command("det", "Solves the determinant of a matrix. Ex: det A", 1, None)
)
command_list.append(Command("dot", "Dot product of 2 matrices. Ex: dot A B", 2, None))
command_list.append(Command("inv", "Invert a matrix is possible. Ex: inv A", 1, None))
command_list.append(Command("set", "Set a variable. Ex: set A rref B", 2, None))
command_list.append(
    Command("print", "Print a variable. Ex: print A", 1, None, is_void=True)
)
command_list.append(Command("help", "Print this help message.", 0, None, True))
command_list.append(Command("quit", "Exit the program.", 0, None, True))
command_list.append(Command("read", "Read variable. Ex: Read A", 1, None))
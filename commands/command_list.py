from commands.command import Command
from commands.linear_algebra_commands import det, dot, rref, inv, transp

from .variables_commands import (
    load_variable,
    read_variable,
    print_value,
    set_variable_command,
    store_variable,
)

command_list = []


def quit(_params):
    return "Bye!", None


def print_help(_params):
    print("Commands:")
    for cmd in command_list:
        print(cmd.name + " - " + cmd.description)
    print()

    return None, None


command_list.append(Command("read", "Read variable. Ex: Read A", 1, read_variable))
command_list.append(
    Command("load", "Load previously saved variable. Ex: load A", 1, load_variable)
)
command_list.append(
    Command("store", "Clear the screen.", 1, store_variable, is_void=True)
)
command_list.append(
    Command("set", "Set a variable. Ex: set A B", 2, set_variable_command)
)
command_list.append(
    Command("print", "Print a variable. Ex: print A", 1, print_value, is_void=True)
)

command_list.append(Command("rref", "Row reduce a matrix. Ex: rref A", 1, rref))
command_list.append(Command("dot", "Dot product of 2 matrices. Ex: dot A B", 2, dot))
command_list.append(Command("inv", "Invert a matrix is possible. Ex: inv A", 1, inv))
command_list.append(Command("transp", "Transpose a matrix. Ex transp A", 1, transp))
command_list.append(
    Command("det", "Solves the determinant of a matrix. Ex: det A", 1, det)
)


command_list.append(
    Command("help", "Print this help message.", 0, print_help, is_void=True)
)
command_list.append(Command("quit", "Exit the program.", 0, quit, is_void=True))

command_list.append(Command("solve", "Solve a system of equations.", 0, None))

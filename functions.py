FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH): # non-default parameters goes in front of default parameters
    with open(filepath, 'w') as file:
        file.writelines(todos_arg) #this function is more like a procedure. It does not retunr anything.It modifies some components in a file.


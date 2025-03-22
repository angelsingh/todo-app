FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """
    Return a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

# print(help(get_todos))
def write_todos(todos_arg,filepath=FILEPATH):
    """Write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print("__name__: ",__name__,", type(__name__): ",type(__name__))

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
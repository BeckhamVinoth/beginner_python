def get_todos(file_path='todos.txt'):
    """
    This will return list of todo items
    """
    with open(file_path, 'r') as file_local:
        todo_list_items = file_local.readlines()
    return todo_list_items


def write_todos(todo_items, file_path='todos.txt'):
    """
    Updating the text file
    """
    with open(file_path, 'w') as file_local:
        file_local.writelines(todo_items)

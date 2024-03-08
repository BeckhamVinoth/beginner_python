import time
current_time = time.strftime("%m-%d-%y : %H:%M:%S")
print("Current time (time):", current_time)


def get_todos(file_path):
    with open(file_path, 'r') as file_local:
        todo_list_items = file_local.readlines()
    return todo_list_items


def write_todos(file_path, todo_items):
    with open(file_path, 'w') as file_local:
        file_local.writelines(todo_items)


show_todo = True

while show_todo:
    user_action = input('Add, Show, Edit, Complete or exit ? ')

    if user_action.startswith('add'):
        todo = f"{user_action[4:]}\n"
        todo_list = get_todos('todos.txt')
        todo_list.append(todo)
        write_todos('todos.txt', todo_list)

    elif user_action.startswith('show'):
        todo_list = get_todos('todos.txt')
        for i, todo in enumerate(todo_list):
            todo = todo.strip('\n')
            print(f"{i+1}-{todo.capitalize()}")

    elif user_action.startswith('edit'):
        try:
            todo_list = get_todos('todos.txt')
            index = int(user_action[5:])
            new_todo = input('Enter new todo : ')
            todo_list[index-1] = f"{new_todo}\n"
            write_todos('todos.txt', todo_list)

        except ValueError:
            print('Query not found !!!')
            continue

    elif user_action.startswith('complete'):
        try:
            todo_list = get_todos('todos.txt')
            item = int(user_action[9:])
            todo_list.pop(item-1)
            write_todos('todos.txt', todo_list)

        except IndexError:
            print('Query not found !!!')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Query not found !!!')
print('Ok, Bye')

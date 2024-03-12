import functions
import PySimpleGUI as psg
import functions

label = psg.Text('Type in a todo')
input_box = psg.InputText(tooltip="Enter todo", key='todo')
add_btn = psg.Button("Add")

edit_btn = psg.Button("Edit")
list_box = psg.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=(45, 10))

window = psg.Window('My ToDo App',
                    layout=[[label], [input_box, add_btn], [list_box, edit_btn]],
                    font=('Helvetica', 20))
while True:
    event, value = window.read()
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case psg.WIN_CLOSED:
            break
        case 'todos':
            curr_todo = value['todos'][0]
            window['todo'].update(value=curr_todo)
        case 'Edit':
            todo_to_edit = value['todos'][0]
            new_todo = value['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)


window.close()

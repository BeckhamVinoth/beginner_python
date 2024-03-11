import functions
import PySimpleGUI as psg
import functions

label = psg.Text('Type in a todo')
input_box = psg.InputText(tooltip="Enter todo", key='todo')
add_btn = psg.Button("Add")

window = psg.Window('My ToDo App',
                    layout=[[label], [input_box, add_btn]],
                    font=('Helvetica', 20))
while True:
    event, value = window.read()
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case psg.WIN_CLOSED:
            break


window.close()

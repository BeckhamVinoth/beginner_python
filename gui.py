import os
import time

import PySimpleGUI as psg

import functions

psg.theme('DarkGreen')

if not os.path.exists("todos.txt"):
    with open('todos.txt', 'w') as file:
        pass

clock = psg.Text('', key='curr_time')
label = psg.Text('Type in a todo')
input_box = psg.InputText(tooltip="Enter todo", key='todo')
add_btn = psg.Button("Add")

edit_btn = psg.Button("Edit")
complete_btn = psg.Button("Complete")
exit_btn = psg.Button("Exit")
list_box = psg.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=(30, 10))

window = psg.Window('My ToDo App',
                    layout=[[clock],
                            [label],
                            [input_box, add_btn],
                            [list_box, edit_btn, complete_btn],
                            [exit_btn]
                            ],
                    font=('Helvetica', 20))
while True:
    event, value = window.read(timeout=200)
    window["curr_time"].update(value=time.strftime("%b%d,%Y : %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            curr_todo = value['todos'][0]
            window['todo'].update(value=curr_todo)
        case 'Edit':
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                psg.popup('Please select something', font=('Helvetica', 20))
        case 'Complete':
            try:
                todo_comp = value['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_comp)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                psg.popup('Please select something', font=('Helvetica', 20))
        case 'Exit':
            break
        case psg.WIN_CLOSED:
            exit()


window.close()

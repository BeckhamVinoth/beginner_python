import functions
import PySimpleGUI as psg

label = psg.Text('Type in a todo')
input_box = psg.InputText(tooltip="Enter todo")
add_btn = psg.Button("Add")

window = psg.Window('My ToDo App', layout=[[label], [input_box, add_btn]])
window.read()
window.close()

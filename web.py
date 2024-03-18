import streamlit
import streamlit as sl
import functions

todos = functions.get_todos()


def add_new():
    if sl.session_state['new_todo'].strip():
        new_todo = sl.session_state['new_todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)


sl.title('My ToDo App')
sl.subheader('We can add and complete ur day today items here')

for i, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del streamlit.session_state[todo]
        streamlit.experimental_rerun()

sl.text_input(label='input',
              label_visibility='hidden',
              placeholder='Type in new todo..',
              key='new_todo',
              on_change=add_new)


sl.session_state

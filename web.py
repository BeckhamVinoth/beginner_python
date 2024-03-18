import streamlit as sl
import functions


todos = functions.get_todos()
sl.title('My ToDo App')
sl.subheader('We can add and complete ur day today items here')

for todo in todos:
    sl.checkbox(todo)

sl.text_input(label='',placeholder='Type in new todo..')




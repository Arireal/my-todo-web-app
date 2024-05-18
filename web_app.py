import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    new_todo_local = st.session_state['new_todo'] + "\n"
    todos.append(new_todo_local)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''



todos = functions.get_todos()

st.title("My Todo App")
st.subheader("Your Personalized To-Do List")
st.write("Stay Organized and Productive with Your Personalized To-Do List")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder=" Add New Todo",
              on_change=add_todo, key='new_todo')



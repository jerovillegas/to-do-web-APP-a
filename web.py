import streamlit as st
import functions
from streamlit_autorefresh import st_autorefresh
import time

limit = time.time()  #función para autorefrescar la página cada 500 milisegundos con un limite indefinido
interval = 2000
count = st_autorefresh(interval=interval, limit=int(limit), key="fizzbuzzcounter")

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""


st.title("To-Do App")

st.subheader("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo + f"{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo + f"{index}"]
        st.experimental_rerun()
st.text_input(label="", placeholder="Add new to-do...", on_change=add_todo, key='new_todo')

import streamlit as st
import functions

todos = functions.getToDos()

def add_todo() :
    todo = st.session_state["newToDo"] + "\n"
    # print(todo)
    todos.append(todo)
    functions.writeToDos(todos)

st.title("My ToDo app")
st.subheader("This is my todo app.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        functions.writeToDos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ", placeholder="Add a todo...",
              on_change=add_todo, key="newToDo")
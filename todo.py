"""
@author: Swapnil Deb
@date: 06/01/2024
This is a fun project 
"""

import streamlit as st
from todoist import Todoist
from streamlit import session_state as state  

# todoist instance
if "todoist" not in state:
    state.todoist = Todoist()

st.header("poopooList 🚀")
st.markdown("---")
st.subheader("Thou shalt name a task 🤖")

# Get the task from the text input field
task = st.text_input("Please keep the human limitations in mind 💀")

if st.button("ADD"):
    if task:
        state.todoist.addTask(task)
        #st.success("Added")
        # Clear the text input field by setting task to an empty string
        task = ""
    # else:
    #     st.error("NOO..Enter a task 💀")

st.markdown("---")

# Display tasks
st.subheader("Tasks 🔧")
tasks_to_remove = []
for i, task in enumerate(state.todoist.todoist):
    if st.checkbox(f"{i+1}. {task}"):
        tasks_to_remove.append(i)

# Button to remove tasks in batch
if st.button("Remove selected"):
    # Remove tasks in reverse order to avoid index changes
    for i in sorted(tasks_to_remove, reverse=True):
        state.todoist.removeTaskAtIndex(i)
    st.experimental_rerun()

st.markdown("---")

st.write("A FUN PROJECT OF MINE")



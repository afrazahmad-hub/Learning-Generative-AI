import streamlit as st
import numpy as np

st.title("Chat Message")

assistant = st.chat_message("assistant")
assistant.bar_chart(np.random.randn(20,3))

user = st.chat_message("user")
user.write("Thanks")



import streamlit as st


st.title("Chat Input")

prompt = st.chat_input("Say Something")

if "data" not in st.session_state:
    st.session_state.data = []


if prompt:
    st.session_state.data.append(prompt)

    st.write(f"User input: {prompt}")


st.write(st.session_state.data)




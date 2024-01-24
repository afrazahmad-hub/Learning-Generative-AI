import streamlit as st

st.title("Expender")

with st.expander("See explanation"):
    st.write("The chart below shows some numbers I picked for you. I rolled actual dice for these, so they're guaranteed to be random.")
    st.image("https://static.streamlit.io/examples/dice.jpg")
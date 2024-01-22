import streamlit as st

st.title("Side Bar")


# Using object notation
st.sidebar.selectbox(
    "How would you like to be connected?",
    ("Email", "Home phone", "Skype")
)


# Using with notation
with st.sidebar:
    st.radio(
        "Choose a shopping method",
        ("Standard (5-15 Days)", "Express (2-3 Days)")
    )

with st.sidebar:
    st.radio(
        "Choose Gender",
        ("Men", "Women", "Other")
    )


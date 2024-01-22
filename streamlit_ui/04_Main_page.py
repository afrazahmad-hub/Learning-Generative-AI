import streamlit as st

# we can add multiple pages
# just create a pages folder, paralel to main file
# we can list the pages, just by assigning the the number to the file i.e. 1_About.py ....

# change the name and Icon of the page
st.set_page_config(
     page_icon="👋",
    page_title="Afraz",
)


st.success("Main Page, Afraz")

# st.sidebar.success("Select a demo above.")

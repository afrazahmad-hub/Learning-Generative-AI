import streamlit as st

#  create a .streamlit folder
#  add file named: secrets.toml in that folder


# Everything is accessible via the st.secrets dict:

st.write("DB Name: ", st.secrets["DB_NAME"])
st.write("DB Passward: ", st.secrets["DB_PASSWORD"])






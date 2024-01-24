import streamlit as st
import time

st.title("Status")

with st.status("Downloading Data.....", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL...")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(label="Download Completed", state="complete", expanded=False)

st.button("Re-run")


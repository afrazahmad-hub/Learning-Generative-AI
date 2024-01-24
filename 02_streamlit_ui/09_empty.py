import streamlit as st
import time


# Inserts a container into your app that can be used to hold a single element. 

with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ 10 seconds over!")

st.write("Hi, I am Afraz Ahmad")





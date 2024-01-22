import streamlit as st
import numpy as np


with st.container():

    st.write("This graph is inside container")

    # create a bar chart of 50 values
    st.bar_chart(np.random.randn(50, 4))

st.write("This is outside container")


 



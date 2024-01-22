import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np


# Through magic feature streamlit identify the type of the data (i.e. list, dict, markdown etc)
# and display it automatically, either we run display command or not
st.write("Magic command")

tb : pd.DataFrame = pd.DataFrame({"Col 1" : [1,2,3],
                                  "Col 2" : ["a", "b", "c"]})


# We can print it in either way
tb 
# st.write(tb)
# st.table(tb)
# st.json(tb.to_dict())
# st.metric("Metric",  42, 2)


x : int = 100
"X =", x # will display X = 100
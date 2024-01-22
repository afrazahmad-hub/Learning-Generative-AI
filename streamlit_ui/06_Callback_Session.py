import streamlit as st

# create a function and use t multiple times

st.title("Session Counter using Callback")

# add counter into session
if 'count' not in st.session_state:
    st.session_state.count = 0


def increment_counter():
    st.session_state.count += 1

#  we can add multiple buttons
#  all will behave same way
st.button("Increment1", on_click=increment_counter)
st.button("Increment2", on_click=increment_counter)
st.button("Increment3", on_click=increment_counter)

st.write("Count:", st.session_state.count)


st.title("Session Counter using Callback with Arguments")

# add session
if 'count2' not in st.session_state:
    st.session_state.count2 = 0

increment_value = st.number_input('Enter a value', value=1, step=1)

def increment_counter(increment_value):
    st.session_state.count2 += increment_value

st.button('Incrementt', on_click=increment_counter,
    args=(increment_value, ))

st.write('Count 2 = ', st.session_state.count2)




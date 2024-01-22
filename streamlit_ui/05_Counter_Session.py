import streamlit as st


# Counter without Session State
# No matter how many times we press the Increment button in 
# the above app, the count remains at 1.
#  Because state is not manages at backend

st.title('Counter Example without Session')
count = 0

increment = st.button('Incrment')
if increment:
    count += 1

st.write('Count = ', count)

st.title("Counter example with session")

# add a session on server
if 'count' not in st.session_state:
    st.session_state.count = 0

Increment = st.button('Increment')

if Increment:
    st.session_state.count += 1

st.write("Count: ", st.session_state.count)


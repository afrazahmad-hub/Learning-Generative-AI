import streamlit as st

st.title("This is the Title")
st.header("This is main Heading")
st.subheader("This is Sub-Heading")
st.write("This is Write command")
st.markdown("# Markdown")
st.markdown("## Markdown")
st.code("Code: [i for i in range(1,10)]")

st.write("Following is the latex, which is used by researcher to write research papers")
st.latex(''''e^{i\pi} + 1 = 0 ''')


st.write("We can also ad  Image / Video / Audio")
# we have added web urls here, but we can also add from our local storage
st.audio("https://pixabay.com/sound-effects/uplifting-pad-texture-113842/")
st.image("https://previews.123rf.com/images/jpcasais/jpcasais0911/jpcasais091100037/5886333-beautiful-light-in-a-green-and-beautiful-forest.jpg")
st.video("https://www.youtube.com/watch?v=IUN664s7N-c")



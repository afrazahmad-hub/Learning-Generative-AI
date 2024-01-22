import streamlit as st
from PIL import Image



# Success / Error / Warning etc. messages 
st.success("Success mesage")
st.warning("Warning mesage")
st.info("Information mesage")
st.error("Error mesage")

exp = ZeroDivisionError("Cannot devided by zero")
st.exception(exp)

# using this we can modify the height and weidth of the image:
# img = Image.open("https://media.istockphoto.com/id/1194692009/photo/cute-happy-7-month-baby-girl-in-diaper-lying-and-playing.jpg?s=1024x1024&w=is&k=20&c=EJ8K63Dv4q1pxzT2qnWl1yLkEDVhOl4KeRKhnQfWtuc=")
# st.image(img, width=300)



# Checkbox

# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show \ Hide"):
    st.write("Welcome to the Website")

# Radio button
    
# first argument is the title of the radio button
# second argument is the options for the radio button

status = st.radio("Gander:",["Male", "Female", "Shemale"])
# st.write(status)

# Conditional statement to print 
# Male if male is selected else print female
# show the result using the success function
if (status == "Male"):
    st.success("Male")
elif (status == "Female"):
    st.success("Female")
else:
    st.success("Shemale")



# Selection box
 
# first argument takes the title of the selectionbox
# second argument takes options
st.selectbox("Hobbies:", ["Reading", "Hiking", "Exercise"])



# Multi select box
 
# first argument takes the box title
# second argument takes the options to show
st.multiselect("Hobbies: ", ["Reading", "Hiking", "Exercise"])

# Create a simple button that does nothing
st.button("Click me for no reason")

if (st.button("about")):
    st.text("Welcome to the wold of GenAI")



# Text Input
 
# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area

name = st.text_input("Enter your name", "enter here....")

if (st.button("Submit")):
    st.title(name)


# slider
 
# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number

level = st.slider("Select the slider:", 1,10)


# print the level
# format() is used to print value 
# of a variable at a specific position
st.text("Selected: {}".format(level))







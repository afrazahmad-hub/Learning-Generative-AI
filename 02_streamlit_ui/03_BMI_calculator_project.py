import streamlit as st


st.title("Welcome to BMI Calculator")

# get weight in kgs
weight = st.number_input("Enter Weight in KGs")

status = st.radio("Select your height formate:", ["cms", "meters", "feet"])

if (status == "cms"):

    height = st.number_input("Enter Height in Centimeters")

    try:
        bmi = st.text(weight / (height/100)**2)
    except:
        st.text("Please Enter Height")

elif (status == "meters"):

    height = st.number_input("Enter Height in Meters")

    try:
        bmi = weight / (height**2)
    except:
        st.text("Please Enter Height")

else:

    height = st.number_input("Enter Height in Meters")

    try:
        bmi = weight / ((height/3.28)**2)
    except:
        st.text("Please Enter Height")


# Print BMI

if (st.button("Calculate BMI")):
    st.text("Your BMI index is {}".format(bmi))

    # interpretation
    if(bmi < 16):
        st.error("You are Extremely Underweigh")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("You are Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("You are Overweight")
    elif(bmi >= 30):
        st.error("You are Extremely Overweight")



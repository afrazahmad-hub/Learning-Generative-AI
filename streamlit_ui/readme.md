# activate conda enviornment

i.e. conda activate openai3_11

# install streamlit

pip install streamlit
streamlit --version

## streamlit documentation / commands

streamlit hello
OR type in google [streamlit cheet sheet](https://docs.streamlit.io/library/cheatsheet)

# Run the file

## copy the path of folder

cd [folder path]
streamlit run helloworld.py

# Documentation of official website

1. In terminal type:
   python -m venv .venv
2. A folder named ".venv" will appear in your project. This directory is where your
   virtual environment and its dependencies are installed.

# Activate your environment

1. In your terminal, activate your environment with one of the following commands,
   depending on your operating system.

   ### Windows command prompt

   .venv\Scripts\activate.bat

2. Once activated, you will see your environment name in parentheses before your
   prompt. "(.venv)"

# Install Streamlit in your environment

1. In the terminal with your environment activated, type:
   pip install streamlit
2. Test that the installation worked by launching the Streamlit Hello example app:
   streamlit hello

# Create a "Hello World" app and run it

1. Create a "Hello World" app and run it
   Create a file named app.py in your project folder.

2. Any time you want to use your new environment, you first need to go to your
   project folder (where the .venv directory lives) and run the command to activate it:
   .venv\Scripts\activate.bat

3. Once activated, you will see your environment's name in parentheses at the beginning of your terminal prompt. "(
   venv)"

4. Run your Streamlit app
   streamlit run app.py

5. To stop the Streamlit server, press Ctrl+C in the terminal.

6. When you're done using this environment, return to your normal shell by typing:
   deactivate

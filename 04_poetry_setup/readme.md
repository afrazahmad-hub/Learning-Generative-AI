# Installation of Poetry

### poetry docs

https://python-poetry.org/docs/
[Poetry Window Installation](https://gist.github.com/Isfhan/b8b104c8095d8475eb377230300de9b0)

## Step-By-Step guide to installing Poetry on Windows:

1. Open Windows Powershell: Navigate to your Start menu, type "Powershell", and select "Windows Powershell" from the search results.

2. Run Installation Command: 
In the Powershell window, paste the following command and press Enter:
Note: If you've installed Python through the Microsoft Store, replace py with python in the command below.

(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

Wait for Installation to Complete: The installation process may take some time depending on your internet connection speed. Let it run until completion.

3. Copy Installation Path: 
Once the installation is complete, it will provide you with a path. Copy this path as you'll need to add it to your user environment variables.
   C:\Users\Afzal\AppData\Roaming\Python\Scripts\poetry

4. Add Path to Environment Variables:
   Right-click on the Start button and select "System".
   In the System window, click on "Advanced system settings" on the left sidebar.
   In the System Properties window, click on the "Environment Variables..." button.
   In the Environment Variables window, under "User variables for [YourUsername]", find the "Path" variable and select it.
   Click on the "Edit..." button.
   In the Edit Environment Variable window, click on "New" and paste the path you copied from the installation process.
   Click "OK" on all open windows to save your changes.
   Close and Reopen Powershell: Close the Powershell window and open a new one.

5. Verify Installation: In the new Powershell window, type poetry --version and press Enter. If Poetry has been successfully installed, you should see its version number printed in the terminal.

You have now successfully installed Poetry on your Windows system. You can start using it for managing your Python projects.

# Working on Poetry with FastAPI

1. Create a new project with following command
   poetry new [project name]
2. Jump in newly created project
   cd [project name]
3. Poetry command to add a new packege
   While installing the packeges, must be in parent folder
   poetry add [packege(s) name]
   poetry add fastapi _uvicorn[standard]_
   poetry.lock file will also appear in folder
4. Create a file to work, in subfolder, which is available with same name of parent folder
   i.e. mian.py etc

5. Run uvicorn server with following command
   poetry run foldername.filename:app --reload
   i.e. poetry run uvicorn fastapi_helloworld.main:app --reload
6. Then write test
   create a test file in test folder
   import testclient from fastapi
7. Run test
   poetry run pytest -v



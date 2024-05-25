[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/32B92nwd)

Setting up your virtual environment:
1. Use the command pip install pipenv to install the virtual environment manager.
    NOTE: If this command isn't working, try py -m pip install pipenv, python -m pip install pipenv, python3 -m pip install pipenv. If none of the following work, look within your C:\Users\<your_user>\AppData\Local\Programs folder and set an entry in the PATH to your current version of python's Script folder (see the next step for more info).
2. Ensure that within your environment variables, there is an entry in PATH for your installed python's Scripts. For example, C:\Users\<your_user>\AppData\Local\Programs\Python\Python312\Scripts. Reload your environment by closing the shell or IDE application.
3. Ensure that your git repository is up to date by pulling the latest commit to approved.
4. Run the command pipenv install --dev, if this command fails, then there was an error in one of the previous steps.
    NOTE: Ensure that when running this command, you are in the root of the git repo. AKA the folder that contains the Pipfile and Pipfile.lock.
5. Set your IDE's interpreter to the virtual environment. This is IDE specific, but for example, in VS code when you are in a python file, there's a version of python that appears in the bottom right corner, click on this and set the interpreter to the python within the virtual environment.
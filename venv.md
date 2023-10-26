# How to use Virtual Environments with Python

1. Create the venv using `python3 -m venv venv`, this will create a folder with all the information needed to start using a virtual environment
2. Activate the virtual environment by calling the activation file like so `source venv/bin/activate`. Now you are in a virtual environment, where you can install any python module seperate from what your system actually has downloaded
3. You can then deactivate the venv by running `deactivate` in the terminal

> You can install modules automatically through a `requirements.txt` file. You can `pip install -r requirements.txt` to install all of the modules, and `pip freeze` if you would like to generate a list of the modules you're using, which can by copy and pasted into your own `requirements.txt`
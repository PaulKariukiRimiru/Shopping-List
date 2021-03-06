"""
Code used to initialize the app module
PEP8 demands that names of constants should be in all caps.
Pylint, as PEP8, expects module level variables to be "constants".
"""
from flask import Flask

# Initialize the app
APP = Flask(__name__, instance_relative_config=True)

from shopping_list_app import views

# Load the config file
APP.config.from_object('config')


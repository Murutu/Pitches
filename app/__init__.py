from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_simplemde import SimpleMDE

#Instances of flask extensions
#Instance of loginManager and using its methods
login_manager = LoginManager()



def create_app(config_name):
    '''
    Function that takes configuration setting key as an argument
    
    Args:
    config_name : name of the configuration to be used
    '''

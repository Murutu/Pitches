from flask import Flask
# from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_simplemde import SimpleMDE

#Instances of flask extensions
#Instance of loginManager and using its methods
login_manager = LoginManager()
db = SQLAlchemy()
login_manager.session_protection = 'strong'





def create_app(config_name):
    '''
    Function that takes configuration setting key as an argument
    
    Args:
    config_name : name of the configuration to be used
    '''
    #Initialisation application
    app = Flask(__name__)
    
    # simple.init_app(app)
    
    # #Creating the app configurations
    app.config.from_object(config_options[config_name])
    
    #Initialsing flask extensions
    
    db.init_app(app)
    login_manager.init_app

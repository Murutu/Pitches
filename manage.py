# Import db from app factory
from app import create_app, db
from flask_script import Manager,Server
from app.models import *

from flask_migrate import Migrate,MigrateCommand

# Creating app instance
app = create_app('test')
app = create_app('development')
app = create_app('production')

# Create manager instance


@manager.shell
def make_shell_context():
    return dict ( app=app, db=db, User=User, Pitch=Pitch, Comment=Comment)

if __name__ == '__main__':
    manager.run()


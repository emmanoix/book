#order of importation 
#python #3rd party packages #local imports
from flask import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
csrf=CSRFProtect()


def createapp():
    from flask_sqlalchemy import SQLAlchemy
    from flask_wtf.csrf import CSRFProtect
    app=Flask(__name__,instance_relative_config=True)
    #from fapp import config
    app.config.from_pyfile('config.py',silent=True)
    from bookapp.models import db
    db.init_app(app)
    csrf.init_app(app)
    migrate=Migrate(app,db)
    return app


app=createapp()
#csrf=CSRFProtect(app)#means that csrf protection is automatically available for all our routes created with app.route as long as it is post request

from bookapp import user_routes,admin_routes,forms,models


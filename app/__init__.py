from config import config_options
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()
bootstrap= Bootstrap()
def create_app():

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options['development'])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # Will add the views and forms
    #register blueprint

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app 

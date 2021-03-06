
from config import config_options
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_simplemde import SimpleMDE


from flask_mail import Mail

db=SQLAlchemy()
bootstrap= Bootstrap()
simple = SimpleMDE()
login_manager= LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

mail = Mail()

def create_app():

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options['development'])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)
    # configure UploadSet
    

    mail.init_app(app)
    # Will add the views and forms


    #register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    


    return app
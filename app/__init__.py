# The __init__.py file makes Python treat directories containing it as modules.
# Furthermore, this is the first file to be loaded in a module,
# so you can use it to execute code that you want to run each time a module is loaded, or specify the submodules to be exported.
from flask import Flask, session

def create_app():
    app = Flask(__name__) 

    app.config['SECRET_KEY']  = 'THIS IS THE SUPER SECRET KEY' # makes client site session secure

    # import routes . = current directory
    from .views import views
    from .auth import auth

    # register the blue prints
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth") # route starts from /auth/

    return app


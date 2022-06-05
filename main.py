from flask import render_template
from app import create_app # whenever app package is imorted, __init__.py is executed.
import flask

app = create_app()

# name = __main__, app = <Flask 'main'>
    # app.debug=True
    # run the app
if __name__ == "__main__":
       print('App is up & running in port {}'.format(5000), ' Flask version : {}'.format(flask.__version__))
       app.run(debug=True) # app.run() disables debugging  
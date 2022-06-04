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

@app.route("/test-route")
def test_route():
    return "test route works , welcome to the blog app"

"""
When no matching url is hit, show this.
@get requests
"""
@app.errorhandler(404)
def http_404_handler(error):
    # return "<h2>404 Error</h2>", 404
    return render_template('error/page_not_found.html', error_message = '404 | Requested Page Not found ')

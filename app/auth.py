# contains route related to authentication like login 
from flask import  render_template, Blueprint

auth = Blueprint('auth', __name__)  # define blue print, auth is just a user friendly name

"""
 Login page for admin
 @get request
"""
@auth.route('/login-page',methods=['get'])
def get_login_page():
    return render_template("admin_login/login.html", title = "Admin Login")

"""
Actual login form submission
Post request
"""
@auth.route('/login', methods=['post'])  
def login() :
    # res_body = make_response('res_body', status_code=200)
    # res_body.headers['Content-Type'] = 'text/plain'
    # res_body.headers['Server'] = 'Foobar'
    # get input values & validate to the database
    # render message
    # username = request.form.get('email')
    # password = request.form.get('password')
    # remember_me = request.form.get('remember')
    # print("Validating user {}".format(username))
    
    error_message = "Invalid Credentials, Please try again!"
    # db logic goes here 
    # if not succeeded
    return render_template("admin_login/login.html", error_message = error_message)
    # if succeeded take to admin dashboard    

"""
get request to logout for admin
should redirect to /
"""
@auth.route('/logout')
def logout():
    return "Logout Page" # have to redirect after killing session or something like that.      
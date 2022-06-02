from flask import Flask, render_template, make_response
import flask

app = Flask(__name__) 
# name = __main__, app = <Flask 'main'>
# app.debug=True

"""
 Renders home page with navbar & Image
 renders home.html [from templates dir]
 @get request
"""
@app.route('/')
def index():
    #  data = {
    #     'title' : 'My blogs in flask',
    #     'home_nav_text' : 'Home'
    #     # ..... more field
    # }
    # return render_template('home.html', **data)

     title,home_nav_text, blogs_nav_text, admin_login_nav_text, search_nav_text = "My Blogs - Powered with flask !", "Home", 'Blogs', 'Admin Login', 'Search'
     template_context = dict(title = title, home_nav_text = home_nav_text, blogs_nav_text = blogs_nav_text,admin_login_nav_text=admin_login_nav_text,search_nav_text=search_nav_text)
     return render_template('home.html', **template_context)
   

"""
Lists of all blogs in the database
Accessible to all the users
@get request 
"""
@app.route('/blogs')
def get_notes():
    return "All of your blogs"

"""
Retrieve specific blog from the d
@Get request
Accessible for all users
"""
@app.route('/blogs/<int:blog_id>')   
def get_note_by_id(blog_id):
    return "Blog with ID : {}".format(blog_id)  

"""
 Login page for admin
 @get request
"""
@app.route('/login-page')
def get_login_page():
    return "Login Page"

"""
Actual login form submission
Post request
"""
@app.route('/login')  
def login() :
    # res_body = make_response('res_body', status_code=200)
    # res_body.headers['Content-Type'] = 'text/plain'
    # res_body.headers['Server'] = 'Foobar'
    return "Logging you in ..."  

"""
get request to logout for admin
should redirect to /
"""
@app.route('/logout')
def logout():
    return "Logout Page" # have to redirect after killing session or something like that.   

"""
When no matching url is hit, show this.
@get requests
"""
@app.errorhandler(404)
def http_404_handler(error):
    # return "<h2>404 Error</h2>", 404
    return render_template('error/page_not_found.html', error_message = '404 | Requested Page Not found ')

# app.add_url_rule('/','index', index) # other way to route request
# run the app
if __name__ == "__main__":
    print('App is up & running in port {}'.format(5000), ' Flask version : {}'.format(flask.__version__))
    app.run(debug=True) # app.run() disables debugging 
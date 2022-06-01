from flask import Flask

app = Flask(__name__) 
# name = __main__, app = <Flask 'main'>
# app.debug=True

"""
 Renders home page with navbar & Image
 @get request
"""
@app.route('/')
def index():
    return "Home Page"

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
@app.route('/login')
def login():
    return "Login Page"

"""
get request to logout for admin
should redirect to /
"""
@app.route('/logout')
def logout():
    return "Logout Page" # have to redirect after killing session or something like that.   

# app.add_url_rule('/','index', index) # other way to route request
# run the app
if __name__ == "__main__":
    print('App is up & running in port {}'.format(5000))
    app.run(debug=True) # app.run() disables debugging 
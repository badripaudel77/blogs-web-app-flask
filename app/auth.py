# contains route related to authentication like login 
from flask import  redirect, render_template, Blueprint, request, url_for, session
from app.db_config import get_connection
import datetime

auth = Blueprint('auth', __name__)  # define blue print, auth is just a user friendly name

"""
 Login page for admin
 @get request
"""
@auth.route('/login-page',methods=['get'])
def get_login_page():
      if session['remember_me'] == True and len(session['username']) >5:
            print(' user is already logged in')
            return redirect(url_for('auth.add_blogs'), code=301)
      return render_template("admin_login/login.html", title = "Admin Login")

"""
Actual login form submission
Post request
"""
@auth.route('/login', methods=['post'])  
def login() :
    form_data = request.form
    username, password, remember_me = form_data.get('email'), form_data.get('password'), form_data.get('remember')
  
    if len(username) < 1 or len(password) <1 :
        return render_template("admin_login/login.html",  error_message = "Please enter all the credentials")

    connection, cursor = get_connection()
    try:
        fetch_query = "SELECT * FROM users WHERE username =%s AND password = %s"
        cursor.execute(fetch_query, (username, password)) # expects more than one value in tuple
        data = cursor.fetchall()
        if len(data) > 0:
            # store username in session
            session['username'] = data[0][1] 
            if remember_me == 'on':
                 session['remember_me'] = True
            return redirect(url_for('auth.add_blogs'), code=301) 

        else:
            return render_template("admin_login/login.html", error_message = "Please enter correct credentials")

    except(ConnectionError, Exception) as error:
        return render_template("admin_login/login.html", error_message = "Something went wrong while fetching records from the database : " + str(error))
    finally:
        cursor.close()
        connection.close() 

"""
get request to logout for admin
should redirect to /
"""
@auth.route('/logout', methods=['get', 'post'])
def logout():
    return "Logout Page" # have to redirect after killing session or something like that.   


@auth.route('/add/blogs', methods=['get', 'post'])
def add_blogs():
    if not session['username']:
          return redirect(url_for('auth.get_login_page'), code=301)
    title,home_nav_text, blogs_nav_text, admin_login_nav_text, search_nav_text,brand_nav_text = "Add your new blogs!", "Home", 'Blogs', 'Admin Login', 'Search','Amigos Blogs'
    template_context = dict(title = title, home_nav_text = home_nav_text, blogs_nav_text = blogs_nav_text,admin_login_nav_text=admin_login_nav_text,search_nav_text=search_nav_text,brand_nav_text = brand_nav_text)
     
    if request.method == 'GET':
        # get data from the form     
        return render_template("admin_login/add_blog.html", **template_context) 
    # if post request, validates & adds to the database    
    creator = session['username'] 
    form_data = request.form
    blog_tilte, blog_content, blog_created_date, blog_created_by = form_data.get('title'), form_data.get('content'), datetime.datetime.now(), creator
    if(len(blog_tilte) <10 or len(blog_content) < 20):
        return render_template("admin_login/add_blog.html", error_message = 'Please give proper title & description.') 

    connection, cursor = get_connection()

    insert_into_blogs_query = 'INSERT INTO blogs(title, content, created_on, creator) values(%s, %s, %s, %s)'

    try:
        cursor.execute(insert_into_blogs_query, ( blog_tilte, blog_content, blog_created_date, blog_created_by))
        connection.commit()    

    except(ConnectionError) as connection_error:
        print("Something went wrong while inserting into database : ", connection_error)

    finally:
        connection.close()
        cursor.close()

     # get data from the form     
    return render_template("admin_login/add_blog.html", success_message = 'Blog create successfully')

    
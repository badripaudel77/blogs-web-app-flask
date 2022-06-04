#  contains all the routes 
#  define as blue print i.e tell that it contains bunch of routes

from flask import render_template, Blueprint, session,redirect, url_for
from app.db_config import get_connection

views = Blueprint('views', __name__)  # define blue print, name = views , we can call it routes as well.

"""
 Renders home page with navbar & Image
 renders home.html [from templates dir]
 @get request
"""
@views.route('/')
def index():
     # set default session
     session['remember_me'] = False
     session['username'] = ''

     title,home_nav_text, blogs_nav_text, admin_login_nav_text, search_nav_text,brand_nav_text = "My Blogs - Powered with flask !", "Home", 'Blogs', 'Admin Login', 'Search','Amigos Blogs'
     template_context = dict(title = title, home_nav_text = home_nav_text, blogs_nav_text = blogs_nav_text,admin_login_nav_text=admin_login_nav_text,search_nav_text=search_nav_text,brand_nav_text = brand_nav_text)
     return render_template('home.html', **template_context)

"""
Lists of all blogs in the database
Accessible to all the users
@get request 
"""
@views.route('/blogs', methods = ['get'])
def get_blogs():
     title,home_nav_text, blogs_nav_text, admin_login_nav_text, search_nav_text,brand_nav_text, all_amigos_blogs_text = "My Blogs - Powered with flask !", "Home", 'Blogs', 'Admin Login', 'Search','Amigos Blogs','All Amigos Blogs'
     template_context = dict(title = title, home_nav_text = home_nav_text, blogs_nav_text = blogs_nav_text,admin_login_nav_text=admin_login_nav_text,search_nav_text=search_nav_text,brand_nav_text = brand_nav_text, all_amigos_blogs_text = all_amigos_blogs_text)
     blogs = []
     connection,cursor  = get_connection() 

     try:
          fetch_blogs_query = "SELECT * FROM blogs"
          cursor.execute(fetch_blogs_query)
          # store the data 
          blogs = cursor.fetchall()
     except(ConnectionError) as connection_error:
        print("Something went wrong while fetching blogs from the database : ", connection_error )
     
     finally:
        cursor.close()
        connection.close()     
     return render_template('blogs/blogs.html', blogs, **template_context)
     

"""
Retrieve specific blog from the d
@Get request
Accessible for all users
"""
@views.route('/blogs/<int:blog_id>')   
def get_blog_by_id(blog_id):
    return "Blog with ID : {}".format(blog_id)       
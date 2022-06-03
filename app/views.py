#  contains all the route 
#  define as blue print i.e tell that it contains bunch of routes

from flask import render_template, Blueprint

views = Blueprint('views', __name__)  # define blue print

"""
 Renders home page with navbar & Image
 renders home.html [from templates dir]
 @get request
"""
@views.route('/')
def index():
    #  data = {
    #     'title' : 'My blogs in flask',
    #     'home_nav_text' : 'Home'
    #     # ..... more field
    # }
    # return render_template('home.html', **data)

     title,home_nav_text, blogs_nav_text, admin_login_nav_text, search_nav_text,brand_nav_text = "My Blogs - Powered with flask !", "Home", 'Blogs', 'Admin Login', 'Search','Amigos Blogs'
     template_context = dict(title = title, home_nav_text = home_nav_text, blogs_nav_text = blogs_nav_text,admin_login_nav_text=admin_login_nav_text,search_nav_text=search_nav_text,brand_nav_text = brand_nav_text)
     return render_template('home.html', **template_context)


"""
Lists of all blogs in the database
Accessible to all the users
@get request 
"""
@views.route('/blogs', methods = ['get'])
def get_notes():
     title,home_nav_text, blogs_nav_text, admin_login_nav_text, search_nav_text,brand_nav_text, all_amigos_blogs_text = "My Blogs - Powered with flask !", "Home", 'Blogs', 'Admin Login', 'Search','Amigos Blogs','All Amigos Blogs'
     template_context = dict(title = title, home_nav_text = home_nav_text, blogs_nav_text = blogs_nav_text,admin_login_nav_text=admin_login_nav_text,search_nav_text=search_nav_text,brand_nav_text = brand_nav_text, all_amigos_blogs_text = all_amigos_blogs_text)
     return render_template('blogs/blogs.html', **template_context)     

"""
Retrieve specific blog from the d
@Get request
Accessible for all users
"""
@views.route('/blogs/<int:blog_id>')   
def get_note_by_id(blog_id):
    return "Blog with ID : {}".format(blog_id)       
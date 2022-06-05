### Description about this project [while learning]

#### Reference : https://overiq.com/flask-101/

### What is flask ? 
 - Flask is a micro framework for Python, meaning it's small and doesn't have large no. of built in modules like in other frameworks like Django or Grails. Flask is also less rigid about how you should structure your application.Unlike framework like Django, where you have to follow the strict rules. In Flask, you are free to structure your application the way you want.

### Create virtual environment in python 
- Isolate the packages in this project from the global environment
- to create virtual environment in python, we use ```virtualenv``` command as ```virtualenv venv``` in project directory, where venv is the name of virtual environment [user friendly name]
- to install virtualenv on mac use ```pip install virtualenv```
- to activate virtualenv run  ```source venv/bin/activate``` and to deactivate use ```deactivate```

### To install Flask inside virtual environment 
- To install Flask inside virtual environment enter the command: ```sudo pip3 install flask``` or ```pip3 install flask``` on project directory not venv dir or `pip install flask==version_number` if specific version.
- to unistall if needed, use ```python3 -m pip uninstall flask ```  
- to verify flask installation we can use following command, it will give the installed version of the flask [2.1.2] as of writing this file
- ```import flask```
- ```print(flask.__version__)```


### __init__.py , load app & run app
- The __init__.py file makes Python treat directories containing it as modules.
- Furthermore, this is the first file to be loaded in a module, so you can use it to execute code that you want to run each time a    module is loaded, or specify the submodules to be exported.

### run app 
- To run app either use ```python main_file.py ``` or ```flask run```
### Define route 
- to define route in flask , we can use ```app.add_url_rule('/', 'index', index)``` where index is the name of the method or 
  use ```route``` decorator as ```@app.route('/')``` 

### Blueprint
- to separate route from the main app, we can create blueprint and later register to that main file in __init__.py
- create blueprint as ```auth = Blueprint('auth', __name__)  # define blue print ``` where Blueprint is imported from flask
- register blue print as : '.views' is the name of blueprint
  ```  from .views import views
       from .auth import auth
  ```     
-  contains all the route 
-  define as blue print i.e tell that it contains bunch of routes

### Can have html files in template folder [templates is default] 
- Can render html page when request [/, / some patters ] using ```render_template``` method as render_template('file_name_in_templates foler', data if any) 
for eg : ``` return render_template('home.html', title='My Blogs - Powered with flask !')```

- To pass many arguments data to the view , use as 
   ```home_nav_text, blogs_nav_text, admin_login_nav_text, search_nav_text = "HOME", 'BLOGS', 'ADMIN LOGIN', 'SEARCH'
     template_context = dict({home_nav_text = home_nav_text, blogs_nav_text = blogs_nav_text,admin_login_nav_text=admin_login_nav_text,search_nav_text=search_nav_text })
     return render_template('home.html', **template_context)
   ``` 
   or create dictionary and pass
    ```
      data = {
        'title' : 'My blogs in flask',
        'home_nav_text' : 'Home'
         # more field
      }
      return render_template('home.html', **data)
    ```
### Creating response
- Even though flask autmatically creates reposne using ```make_response()``` , but often we need to include more options like header , content-type etc, 
- syntax of make_response is 
```res_obj = make_response(res_body, status_code=200) ```
- to set additional type , we can use ``` res_obj``` as 
  ``` res.headers['Content-Type'] = 'text/plain' ```
  ``` res.headers['Server'] = 'Foobar ' ```  

### Redirect the reponse
- to redirect the response, we can use ```return redirect("url_to_redirect", code=301)```  
- To include template from one file or directory in another we can use , ``` include ``` statement in flask as 
``` {% include 'path/to/template' %} ```   

### Intercepting requests
- Just like grails [& other langaguages too] has interceptor, python also some decorators like ``` before_first_request, after_request etc ``` can be used as 
```
@app.before_request
def before_request():
    print("before_request() called")
```
### Aborting requests 
``` @app.route('/')
    def abort_this_request():
          abort(404)
```
### serving static files
- static files like .css , .js files are included in 'flask_app/static' directory  by default , if different, have to configure.
- to use that files, use ```    <link rel="stylesheet" href="{{ url_for('static', filename='nav_styles.css') }}">```

### custom error handler
- have ```errorhandler``` decorator to show custom pages
- can be used as ```@app.errorhandler(404)``` where 404 is the code passed to indicate not found

### connecting to database 
- without using ORM tools 
- There are several python modules that allow us to connect to and manipulate the database using PostgreSQL, one of them  is  Psycopg2
- To install Psycopg2, we can run the command 
 ```sudo pip3 install psycopg2``` 
- once installed, we can import it and get various available methods.

### To share [Extract required dependencies in requirements.txt file]
- use command in project directory ```pip freeze > requirements.txt```



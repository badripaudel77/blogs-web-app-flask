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
- To install Flask inside virtual environment enter the command: ```sudo pip3 install flask``` or ```pip3 install flask``` on project directory not venv dir
- to verify flask installation we can use following command, it will give the installed version of the flask [2.1.2] as of writing this file
     - >>> import flask
     - >>> flask.__version__

### Define route 
- to define route in flask , we can use ```app.add_url_rule('/', 'index', index)``` where index is the name of the method or 
  use ```route``` decorator as ```@app.route('/')```     
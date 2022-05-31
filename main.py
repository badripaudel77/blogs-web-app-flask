from flask import Flask

app = Flask(__name__) # name = __main__, app = <Flask 'main'>
# app.debug=True

@app.route('/')
def index():
    return "Home Page"

@app.route('/login')
def login():
    return "Login Page"

@app.route('/logout')
def logout():
    return "Logout Page" # have to redirect after killing session or something like that.

@app.route('/notes')
def get_notes():
    return "All of your notes"

@app.route('/notes/<int:note_id>')   
def get_note_by_id(note_id):
    return "This your note with ID : {}".format(note_id)     

# app.add_url_rule('/','index', index) # other way to route request
# run the app
if __name__ == "__main__":
    print('App is up & running in port {}'.format(5000))
    app.run(debug=True) # app.run() disables debugging 
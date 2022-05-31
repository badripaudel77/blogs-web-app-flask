from flask import Flask

app = Flask(__name__) # name = __main__, app = <Flask 'main'>

@app.route('/')
def index():
    return "hello world !"

# run the app
if __name__ == "__main__":
    print('App is up & running in port {}'.format(5000))
    app.run(debug=True) # app.run() disables debugging 
# import the flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True


# use the decorator pattern to
# link the view function to a url
@app.route("/")
@app.route("/hello")
# define the view using a function, which returns a string
def hello_world():
    return("Hello, world!?!?!?!?!?")


# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return(search_query)


# dynamic route with explicit status coddes
@app.route("/name/<name>")
def index(name):
    if name.lower == "michael":
        return "Hello, {}".format(name), 200
    else:
        return "Not Found", 404


# start the development surver using the run() method
if __name__ == "__main__":
    app.run()

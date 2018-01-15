from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def hello_world():
    return("Hello, world!")


@app.route("/test/<search_query>")
def search(search_query):
    return(search_query)


@app.route("/integer/<int:value>")
def int_type(value):
    return(value, "Next is:", value + 1, "Correct")


@app.route("/float/<float:value>")
def float_type(value):
    return(value)
    return("Next is:")
    return(value + 1)
    return("Correct")


@app.route("/path/<path:value>")
def path_type(value):
    return(value)
    return("Correct")


if __name__ == "__main__":
    app.run()

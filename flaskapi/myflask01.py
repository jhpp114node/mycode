#!/usr/bin/env python3

from flask import Flask

# Flask constructor to tkae the name of current
app = Flask(__name__)


# route() function of the Flask class is a
# decorator, tell the application which url
# should call the associated function

@app.route("/")
def hello_world():
    return "Hello World"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) # runs the application
    # app.run(host="0.0.0.0", port=2224, debug=True) # debug mode

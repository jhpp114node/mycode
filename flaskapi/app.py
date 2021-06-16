## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template


# basic set-up
app = Flask(__name__)

# path /
# path /start
@app.route("/")
@app.route("/start")
def start():
    return render_template("postmaker.html")

# you can have to more than single http request
@app.route("/login", methods=["GET", "POST"])
def login():
    # Post would likely come from a suser interacting with postmaker.html
    if request.method == "POST":
        # it retrieve the name value
        if request.form.get("nm"):
            # nm exist
            username = request.form.get("nm")
        else:
            username = 'guest'
    # Get request
    elif request.method == "GET":
        if request.args.get("nm"):
            # pull nm from localhost:5060/login?nm=larry
            username = request.args.get("nm")
        else:
            # if nm was not passed
            username = "guest"
    # I like this way better
    return redirect(f"/success/{username}")


# path after login
@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) # runs the application

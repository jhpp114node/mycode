from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import escape
from flask import request

app = Flask(__name__)
app.secret_key = "any random string"

@app.route("/")
def index():
    if "username" in session:
        username = session.get("username")
        return f"Logged in as {username} </br><a href='/logout'>click to logout<a/>"
    # if the key username does not have a value in session
    return "You are not logged in</br><a href='/login'>click here to login</a>"


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        return redirect("/")
    return """
       <form action = "" method = "post">
          <p><input type = text name = username></p>
          <p><input type = submit value = Login></p>
       </form>
      """

@app.route("/logout", methods=["GET", "POST"])
def logout():
    # remove the username from the ssion if it is there
    # clear out the session
    session.pop("username", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2225)

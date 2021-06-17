from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

app = Flask(__name__)


# route to root
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/check', methods=["GET","POST"])
def check():
    VALID_INPUT = "good morning"
    if request.method == "POST":
        user_input = request.form.get("question").lower()
        if user_input == VALID_INPUT:
            return redirect("/correct")
        else:
            return redirect("/")
    if request.method == "GET":
        user_input = request.args.get("question").lower()
        if user_input == VALID_INPUT:
            return redirect("/correct")
        else:
            return redirect("/")


@app.route('/correct')
def correct():
    return "Good morning!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)


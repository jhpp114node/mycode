from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

# ###############################
# ##########GIVEN DATA###########
groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]


app = Flask(__name__)
app.secret_key = "I am super secret"


@app.route('/')
def index():
    # check if the user has session
    permission = session.get("permission-w")
    return render_template("index.html", group_data=groups)


@app.route('/permission')
def get_permission():
    if "permission-w" in session:
        print("Session Exist")
        return redirect(url_for("index"))
    session["permission-w"] = "w"
    return redirect(url_for("index"))


@app.route('/add', methods=["GET", "POST"])
def add_group():
    if request.method == "POST":
        hostname = request.form.get("hostname")
        ip = request.form.get("ip")
        fqdn = request.form.get("fqdn")
        new_data_map = {
            "hostname":hostname,
            "ip":ip,
            "fqdn":fqdn
        }
        groups.append(new_data_map)
        print("Successfully added")
        return redirect(url_for("index"))


@app.route('/destroy_permission')
def destroy_permission():
    if 'permission-w' in session:
        session.pop('permission-w')
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2225)

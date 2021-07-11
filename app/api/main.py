from flask import Flask, render_template
from extensions.register import register
from extensions.login import login
from extensions.update import update
from extensions.delete import delete
from extensions.getusers import getusers

app = Flask("first-app", template_folder="template")
app.register_blueprint(register)
app.register_blueprint(login)
app.register_blueprint(update)
app.register_blueprint(delete)
app.register_blueprint(getusers)


@app.route("/", methods=["GET"])
def home_page():
    return render_template("index.html")


app.run(debug=True)

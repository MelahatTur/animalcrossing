from flask import Flask
from flask import render_template
from .utils.db import init_db
from .controllers import auth_controller, dashboard_controller

init_db()

app = Flask(__name__)
app.secret_key = 'dev'

@app.route("/")
def homepage():
    return render_template("homepage.html")

app.register_blueprint(auth_controller.auth_bp)
app.register_blueprint(dashboard_controller.dashboard_bp)
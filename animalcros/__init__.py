from flask import Flask
from flask import render_template

from .utils.db import init_db, load_collectables, load_availability
from .controllers import auth_controller, dashboard_controller, collectable_controller


init_db()
load_collectables()
load_availability()

app = Flask(__name__)
app.secret_key = 'dev'

@app.route("/")
def homepage():
    return render_template("homepage.html")

app.register_blueprint(auth_controller.auth_bp)
app.register_blueprint(dashboard_controller.dashboard_bp)
app.register_blueprint(collectable_controller.collectable_bp)

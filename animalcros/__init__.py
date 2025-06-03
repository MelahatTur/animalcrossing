from flask import Flask
from .utils.db import init_db
from .controllers import auth_controller, dashboard_controller

init_db()

app = Flask(__name__)
app.secret_key = 'dev'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.register_blueprint(auth_controller.auth_bp)
app.register_blueprint(dashboard_controller.dashboard_bp)
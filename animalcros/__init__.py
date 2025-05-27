#initialise program
from flask import Flask
from .utils.db import init_db
from .controllers import category, todo

init_db()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.register_blueprint(todo.bp)
app.register_blueprint(category.bp)
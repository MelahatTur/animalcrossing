from flask import Blueprint, render_template, redirect, url_for, session, flash
from animalcros.forms import RegisterForm, LoginForm
from animalcros.models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.get_user_by_username(form.username.data):
            flash("Username already exists.")
            return redirect(url_for("auth.register"))

        User.create_user(form.username.data, form.password.data)
        flash("Registration successful. Please log in.")
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_user_by_username(form.username.data)
        if user and user.password == form.password.data:
            session["user_id"] = user.id
            session["username"] = user.username
            flash("Login successful.")
            return redirect(url_for("hello_world"))
        flash("Invalid username or password.")
    return render_template("login.html", form=form)

@auth_bp.route("/logout")
def logout():
    user_id = session.get("user_id")
    if user_id:
        User.delete_user_by_id(user_id)  # You’ll create this method in your model
    session.clear()
    flash("Logged out and user deleted.")
    return redirect(url_for("auth.login"))

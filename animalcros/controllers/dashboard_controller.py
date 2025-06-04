from flask import Blueprint, render_template, session, redirect, url_for
from animalcros.models.collection import get_collection_progress

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def user_dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    username = session.get("username")
    user_id = session.get("user_id")

    progress_data = get_collection_progress(user_id)

    return render_template(
        "dashboard.html",
        username=username,
        collected=progress_data["collected_items"],
        collected_count=progress_data["collected"],
        total=progress_data["total"],
        progress=progress_data["progress"]
    )
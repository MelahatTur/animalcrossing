from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from animalcros.models.collection import search_collectables, add_to_user_collection

collectable_bp = Blueprint("collectable", __name__)

@collectable_bp.route("/collectables", methods=["GET", "POST"])
def collectables():
    user_id = session.get("user_id")
    
    if request.method == "POST":
        collectable_id = request.form.get("collectable_id")
        if user_id and collectable_id:
            success, message = add_to_user_collection(user_id, int(collectable_id))
            flash(message)  # Show message to user (success or error)
        else:
            flash("Missing user or collectable information.")
        return redirect(url_for("collectable.collectables"))
    
    # GET request — fetch filtered collectables
    query = request.args.get("query", "").strip()
    month = request.args.get("month", "").strip()
    ctype = request.args.get("type", "").strip()
    hemisphere = request.args.get("hemisphere", "NH")

    results = search_collectables(query, month, ctype, hemisphere)

    return render_template(
        "collectable.html",
        results=results,
        query=query,
        month=month,
        ctype=ctype,
        hemisphere=hemisphere
    )
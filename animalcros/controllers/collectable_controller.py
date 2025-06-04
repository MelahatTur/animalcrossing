from flask import Blueprint, render_template, request
from animalcros.models.collectable import Collectable

collectable_bp = Blueprint("collectable", __name__)

@collectable_bp.route("/collectables")
def collectables():
    query = request.args.get("query", "")
    month = request.args.get("month", "")
    ctype = request.args.get("type", "")

    results = Collectable.search(query, month, ctype)

    return render_template(
        "collectable.html",
        results=[c.__dict__ for c in results],
        query=query,
        month=month,
        ctype=ctype
    )

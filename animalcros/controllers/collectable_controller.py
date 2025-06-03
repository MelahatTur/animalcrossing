from flask import Blueprint, render_template, request
import csv
import os
import urllib.parse  # Correct import for parsing URLs

collectable_bp = Blueprint("collectable", __name__)

def load_collectables():
    data = []
    base_path = os.path.join(os.path.dirname(__file__), "..", "data")

    month_fields = [
        "NH Jan", "NH Feb", "NH Mar", "NH Apr", "NH May", "NH Jun",
        "NH Jul", "NH Aug", "NH Sep", "NH Oct", "NH Nov", "NH Dec"
    ]

    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    for filename, ctype in [
        ("fish.csv", "Fish"),
        ("insects.csv", "Bug"),
        ("seacreatures.csv", "Sea Creature")
    ]:
        path = os.path.join(base_path, filename)
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Extract Icon Filename from Icon Image URL
                icon_url = row.get("Icon Image", "")
                if icon_url:
                    parsed = urllib.parse.urlparse(icon_url)
                    row["Icon Filename"] = os.path.basename(parsed.path)

                # Build synthetic "Months" field
                available_months = []
                for i, field in enumerate(month_fields):
                    val = row.get(field, "").strip().lower()
                    if val in ("yes", "true", "1", "all day"):
                        available_months.append(month_names[i])

                row["Months"] = ", ".join(available_months)
                row["Type"] = ctype
                data.append(row)

    return data

@collectable_bp.route("/collectables")
def collectables():
    query = request.args.get("query", "").lower()
    month = request.args.get("month", "")
    ctype = request.args.get("type", "")

    all_collectables = load_collectables()
    results = []

    for item in all_collectables:
        name = item.get("Name", "").lower()
        months = item.get("Months", "").lower()
        item_type = item.get("Type", "").lower()

        name_matches = query in name
        type_matches = (ctype == "" or item_type == ctype.lower())
        month_matches = (month == "" or month.lower() in months)

        if name_matches and type_matches and month_matches:
            results.append(item)

    return render_template(
        "collectable.html",
        results=results,
        query=query,
        month=month,
        ctype=ctype
    )

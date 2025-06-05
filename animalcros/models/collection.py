from animalcros.utils.db import db_connection
from urllib.parse import urlparse
import os


def get_user_collected(user_id):
    conn = db_connection()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT c.name, c.image, c.type
            FROM user_collection uc
            JOIN collectables c ON uc.collectable_id = c.id
            WHERE uc.user_id = %s
        """, (user_id,))
        rows = cur.fetchall()
    conn.close()

    # Convert tuples to dicts with keys matching your template
    collected_items = [{"name": r[0], "image": r[1], "type": r[2]} for r in rows]
    return collected_items

def add_to_user_collection(user_id, collectable_id):
    conn = db_connection()
    with conn.cursor() as cur:
        # Check if already collected
        cur.execute(
            "SELECT 1 FROM user_collection WHERE user_id = %s AND collectable_id = %s",
            (user_id, collectable_id)
        )
        if cur.fetchone():
            return False, "You have already collected this item."

        # Insert new collection item
        cur.execute(
            "INSERT INTO user_collection (user_id, collectable_id) VALUES (%s, %s)",
            (user_id, collectable_id)
        )
    conn.commit()
    conn.close()
    return True, "Item successfully added to your collection."

def remove_from_user_collection(user_id, collectable_id):
    conn = db_connection()
    conn.execute(
        "DELETE FROM user_collection WHERE user_id = %s AND collectable_id = %s",
        (user_id, collectable_id)
    )
    conn.commit()

def get_total_collectables():
    conn = db_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM collectables")
        return cur.fetchone()[0]

def get_collection_progress(user_id):
    total = get_total_collectables()
    collected = get_user_collected(user_id)
    return {
        "total": total,
        "collected": len(collected),
        "progress": round((len(collected) / total) * 100) if total else 0,
        "collected_items": collected
    }

def extract_filename_from_url(url):
    if not url:
        return ""
    path = urlparse(url).path
    return os.path.basename(path)


def search_collectables(query=None, month=None, ctype=None, hemisphere="NH"):
    conn = db_connection()
    with conn.cursor() as cur:
        conditions = []
        params = []

        if query:
            conditions.append("LOWER(c.name) LIKE %s")
            params.append(f"%{query.lower()}%")
        
        if ctype:
            conditions.append("LOWER(c.type) = %s")
            params.append(ctype.lower())

        if month:
            conditions.append("""
                c.id IN (
                    SELECT a.collectable_id
                    FROM availability a
                    WHERE LOWER(a.month) = %s AND a.hemisphere = %s
                )
            """)
            params.extend([month.lower(), hemisphere])

        where_clause = "WHERE " + " AND ".join(conditions) if conditions else ""

        query_sql = f"""
            SELECT
                c.id,
                c.name,
                c.image,
                c.type,
                c.price,
                c.description,
                string_agg(DISTINCT a.month, ', ') AS months_available,
                string_agg(DISTINCT a.hemisphere, ', ') AS hemispheres_available,
                string_agg(DISTINCT a.time_of_day, ', ') AS times_of_day_available
            FROM collectables c
            LEFT JOIN availability a ON c.id = a.collectable_id
            {where_clause}
            GROUP BY c.id, c.name, c.image, c.type, c.price, c.description
            ORDER BY c.name
        """

        cur.execute(query_sql, params)
        results = cur.fetchall()

        # Process image filename as before
        processed_results = []
        for r in results:
            id_, name, image_url, type_, price, desc, months, hemispheres, times = r
            image_filename = extract_filename_from_url(image_url)
            processed_results.append(
                (id_, name, image_filename, type_, price, desc, months, hemispheres, times)
            )

        return processed_results
from animalcros.utils.db import db_connection


def get_user_collected(user_id):
    conn = db_connection()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT c.name, c.image, c.type
            FROM user_collection uc
            JOIN collectables c ON uc.collectable_id = c.id
            WHERE uc.user_id = %s
        """, (user_id,))
        return cur.fetchall()

def add_to_user_collection(user_id, collectable_id):
    conn = db_connection()
    try:
        conn.execute(
            "INSERT INTO user_collection (user_id, collectable_id) VALUES (%s, %s)",
            (user_id, collectable_id)
        )
        conn.commit()
        return True
    except Exception:
        # Could log or handle duplicate entry error here
        return False

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

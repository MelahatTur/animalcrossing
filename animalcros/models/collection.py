from animalcros.utils.db import db_connection

def get_user_collection(user_id):
    db = db_connection()
    return db.execute(
        """
        SELECT c.* FROM collectables c
        JOIN user_collection uc ON c.id = uc.collectable_id
        WHERE uc.user_id = %s
        """,
        (user_id,)
    ).fetchall()

def add_to_user_collection(user_id, collectable_id):
    db = db_connection()
    try:
        db.execute(
            "INSERT INTO user_collection (user_id, collectable_id) VALUES (%s, %s)",
            (user_id, collectable_id)
        )
        db.commit()
        return True
    except Exception:
        # Could log or handle duplicate entry error here
        return False

def remove_from_user_collection(user_id, collectable_id):
    db = db_connection()
    db.execute(
        "DELETE FROM user_collection WHERE user_id = %s AND collectable_id = %s",
        (user_id, collectable_id)
    )
    db.commit()

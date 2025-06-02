from animalcros.utils.db import db_connection

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get_user_by_username(username):
        conn = db_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE username = %s", (username,))
            row = cur.fetchone()
        conn.close()
        if row:
            return User(row[0], row[1], row[2])
        return None

    @staticmethod
    def get_user_by_id(user_id):
        conn = db_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            row = cur.fetchone()
        conn.close()
        if row:
            return User(row[0], row[1], row[2])
        return None

    @staticmethod
    def create_user(username, password):
        conn = db_connection()
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id",
                    (username, password)
                )
                user_id = cur.fetchone()[0]
        conn.close()
        return User(user_id, username, password)
    
    @staticmethod
    def delete_user_by_id(user_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        cursor.close()
        conn.close()
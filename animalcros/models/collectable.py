from animalcros.utils.db import db_connection

class Collectable:
    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.type = row[2]
        self.sell = row[3]
        self.months = row[4:16]  # Assuming months are in positions 4–15

    @staticmethod
    def search(query="", month="", ctype=""):
        conn = db_connection()
        with conn.cursor() as cur:
            sql = """
            SELECT * FROM collectables
            WHERE LOWER(name) LIKE %s
            AND (%s = '' OR LOWER(type) = LOWER(%s))
            AND (
                %s = '' OR
                %s IN (
                    LOWER("NH Jan"), LOWER("NH Feb"), LOWER("NH Mar"), LOWER("NH Apr"),
                    LOWER("NH May"), LOWER("NH Jun"), LOWER("NH Jul"), LOWER("NH Aug"),
                    LOWER("NH Sep"), LOWER("NH Oct"), LOWER("NH Nov"), LOWER("NH Dec")
                )
            )
            """

            like_query = f"%{query.lower()}%"
            cur.execute(sql, (like_query, ctype, ctype, month.lower(), month.lower()))
            rows = cur.fetchall()
        conn.close()
        return [Collectable(row) for row in rows]

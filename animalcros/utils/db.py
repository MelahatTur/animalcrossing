import psycopg2
import os
import pandas as pd
from .import_data import preprocess_collectables

# Try to get from system enviroment variable
# Set your Postgres user and password as second arguments of these two next function calls
user = os.environ.get('PGUSER', 'postgres')
password = os.environ.get('PGPASSWORD', '123')
host = os.environ.get('HOST', '127.0.0.1')

def db_connection():
    db = "dbname='todo' user=" + user + " host=" + host + " password =" + password
    conn = psycopg2.connect(db)

    return conn

def init_db():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # folder of db.py, e.g. /code/animalcros/utils
    schema_path = os.path.join(base_dir, 'schema.sql')      # full path to schema.sql
    with open(schema_path, 'r') as f:
        sql = f.read()

    conn = db_connection()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()

def load_collectables():
    df = preprocess_collectables()

    conn = db_connection()
    cur = conn.cursor()

    for _, row in df.iterrows():
        print(f"Inserting: {row['name']} - {row.get('description')}")
        cur.execute("""
            INSERT INTO collectables (name, image, type, price, description)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING
        """, (
            row.get('name'),
            row.get('image'),
            row.get('type'),
            int(row['price']) if pd.notna(row.get('price')) else 0,
            row.get('description')
        ))

    conn.commit()
    cur.close()
    conn.close()

def load_availability():
    combined_df = preprocess_collectables()

    availability_data = []
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    conn = db_connection()
    cur = conn.cursor()

    for _, row in combined_df.iterrows():
        name = row['name']

        # Fetch collectable_id from the database
        cur.execute("SELECT id FROM collectables WHERE name = %s", (name,))
        result = cur.fetchone()
        if not result:
            continue
        collectable_id = result[0]

        for hemi in ['NH', 'SH']:
            for month in months:
                col = f"{hemi} {month}"
                time_str = row.get(col)

                if pd.notna(time_str) and time_str.strip().lower() not in ['na', 'nan', '']:
                    availability_data.append((collectable_id, month, hemi, time_str.strip()))

    if availability_data:
        cur.executemany("""
            INSERT INTO availability (collectable_id, month, hemisphere, time_of_day)
            VALUES (%s, %s, %s, %s)
        """, availability_data)

    conn.commit()
    conn.close()

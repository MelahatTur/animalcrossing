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
    base_dir = os.path.dirname(os.path.abspath(__file__))  
    schema_path = os.path.join(base_dir, 'schema.sql')      
    with open(schema_path, 'r') as f:
        sql = f.read()

    conn = db_connection()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    
def load_all_data():
    df = preprocess_collectables()
    conn = db_connection()
    cur = conn.cursor()

    # Insert collectables 
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO collectables (name, image, type, price, description)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (name) DO NOTHING
        """, (
            row.get('name'),
            row.get('image'),
            row.get('type'),
            int(row['price']) if pd.notna(row.get('price')) else 0,
            row.get('description')
        ))

    availability_data = []
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    for _, row in df.iterrows():
        cur.execute("SELECT id FROM collectables WHERE name = %s", (row['name'],))
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

    # Insert or update availability
    if availability_data:
        cur.executemany("""
            INSERT INTO availability (collectable_id, month, hemisphere, time_of_day)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (collectable_id, month, hemisphere) DO UPDATE
            SET time_of_day = EXCLUDED.time_of_day
        """, availability_data)

    conn.commit()
    cur.close()
    conn.close()

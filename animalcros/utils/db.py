import psycopg2
import os

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
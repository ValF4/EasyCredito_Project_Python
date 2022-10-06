import main, json, psycopg2
from datetime import datetime

def db_connect():
    _host = "localhost"
    _port = 15432
    _user = "postgres"
    _pass = "postgres"

    return psycopg2.connect(host=_host, port=_port, user=_user, password=_pass)

def execute_query_insert(query):
    conn = db_connect()
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    finally:
        conn.close()

if __name__ == "__main__":
    db_connect()
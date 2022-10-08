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


def execute_query_select(query):
    conn = db_connect()
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        list = []
        for element in records:
            product = main.Product()
            product.name = element[0]
            product.price = element[1]
            product.url = element[2]
            list.append(product)
        return list
    except Exception as e:
        print(e)
    finally:
        conn.close()


def insert_products(products):
    for product in products:
        query = f"INSERT INTO public.products ( name, price, url) VALUES ('{product.name}', {product.price}, '{product.url}')"
        execute_query_insert(query)

if __name__ == "__main__":
    db_connect()
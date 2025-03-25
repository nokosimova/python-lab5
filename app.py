from flask import Flask, request
from datetime import datetime
import psycopg2
import time

app = Flask(__name__)

def database_init():
    retries = 5
    while retries:
        try:
            conn = psycopg2.connect(
                host='db',
                database='counter_db',
                user='user',
                password='password'
            )
            csr = conn.cursor()
            csr.execute("""
                CREATE TABLE IF NOT EXISTS counter (
                    id SERIAL PRIMARY KEY,
                    datetime TIMESTAMP NOT NULL,
                    client_info TEXT NOT NULL
                )
            """)
            conn.commit()
            csr.close()
            conn.close()
            print("База успешно создана.")
            break
        except Exception as e:
            print(f"Ошибка соединения к базе: {e}. Повторяем...")
            time.sleep(3)
            retries -= 1

@app.route('/')
def hello():
    try:
        conn = psycopg2.connect(
            host='db',
            database='counter_db',
            user='user',
            password='password'
        )
        csr = conn.cursor()
        csr.execute(
            "INSERT INTO counter (datetime, client_info) VALUES (%s, %s)",
            (datetime.now(), request.headers.get('User-Agent'))
        )
        conn.commit()
        csr.execute("SELECT COUNT(*) FROM counter")
        count = csr.fetchone()[0]
        csr.close()
        conn.close()
        return f'Привет мир! Меня посмотрели {count} пользователей.\n'
    except Exception as e:
        return f"Ошибка: {e}\n"

if __name__ == "__main__":
    database_init()
    app.run(host='0.0.0.0', port=5000)
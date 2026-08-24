from fastapi import FastAPI
import os
import mysql.connector
from mysql.connector import Error
import socket

app = FastAPI()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.on_event("startup")
def on_startup():
    # Создаём таблицу requests, если её нет
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS requests (
            id INT AUTO_INCREMENT PRIMARY KEY,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            host VARCHAR(255),
            path VARCHAR(255)
        )
        """
        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
        conn.close()
    except Error as e:
        print(f"Error creating table: {e}")

@app.get("/")
def root():
    host = socket.gethostname()
    
    # Вставляем запись в БД
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        insert_query = "INSERT INTO requests (host, path) VALUES (%s, %s)"
        cursor.execute(insert_query, (host, "/"))
        conn.commit()
        cursor.close()
        conn.close()
    except Error as e:
        print(f"Error inserting data: {e}")
        # Даже если ошибка БД, всё равно возвращаем ответ, чтобы curl не падал

    return {"status": "ok", "host": host}

@app.get("/health")
def health():
    return {"health": "ok"}


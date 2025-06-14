# scripts/wait_for_db.py
import time
import psycopg2
import os

from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

for _ in range(10):
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        print("Database is ready!")
        break
    except psycopg2.OperationalError:
        print("Waiting for database...")
        time.sleep(2)

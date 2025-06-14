import sys
import time
import psycopg2
from psycopg2 import OperationalError


def wait_for_db():
    max_retries = 10
    retry_delay = 2

    for attempt in range(max_retries):
        try:
            conn = psycopg2.connect(
                dbname="todo_db",
                user="user",
                password="password",
                host="db"
            )
            conn.close()
            print("✅ PostgreSQL está pronto!")
            return True
        except OperationalError as e:
            print(f"⏳ Tentativa {attempt + 1}/{max_retries} - PostgreSQL não está pronto...")
            time.sleep(retry_delay)

    print("❌ Não foi possível conectar ao PostgreSQL após várias tentativas")
    return False


if __name__ == "__main__":
    if not wait_for_db():
        sys.exit(1)
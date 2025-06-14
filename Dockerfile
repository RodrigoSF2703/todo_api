FROM python:3.9

WORKDIR /app

# Copia primeiro os requirements para aproveitar cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia a pasta scripts primeiro
COPY scripts/ scripts/

# Depois copia todo o resto
COPY app/ app/

# Garante que o script é executável
RUN chmod +x scripts/wait_for_db.py

CMD ["bash", "-c", "python scripts/wait_for_db.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
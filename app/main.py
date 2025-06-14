from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import tasks, auth
from app.database import engine, Base
import time
import sqlalchemy.exc


# Função para tentar conectar ao banco com retry
def wait_for_db():
    max_retries = 5
    retry_delay = 2

    for attempt in range(max_retries):
        try:
            Base.metadata.create_all(bind=engine)
            return
        except sqlalchemy.exc.OperationalError:
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            raise


wait_for_db()

app = FastAPI(
    title="Todo API",
    description="API de gerenciamento de tarefas",
    version="1.0.0"
)

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
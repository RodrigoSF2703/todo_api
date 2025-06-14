from fastapi import APIRouter, Depends, HTTPException, Header, status
from typing import List
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, Task as TaskSchema

router = APIRouter(tags=["tasks"])


# Autenticação com token estático
def verify_token(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Formato de token inválido"
        )

    token = authorization.split(" ")[1]
    if token != "secret-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de autenticação inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return True  # Autenticação válida


# CRUD Implementation
@router.post("/", response_model=TaskSchema, status_code=status.HTTP_201_CREATED)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    _=Depends(verify_token)
):
    db_task = Task(**task.dict(), owner_id=1)  # Fornece um owner_id padrão
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@router.get("/", response_model=List[TaskSchema])
def read_tasks(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db),
        _=Depends(verify_token)
):
    """
    Lista todas as tarefas com paginação.
    - **skip**: Quantidade de itens para pular
    - **limit**: Limite de itens por página
    """
    tasks = db.query(Task).offset(skip).limit(limit).all()
    return tasks


@router.get("/{task_id}", response_model=TaskSchema)
def read_task(
        task_id: int,
        db: Session = Depends(get_db),
        _=Depends(verify_token)
):
    """
    Obtém uma tarefa específica por ID.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )
    return task


@router.put("/{task_id}", response_model=TaskSchema)
def update_task(
        task_id: int,
        task: TaskUpdate,
        db: Session = Depends(get_db),
        _=Depends(verify_token)
):
    """
    Atualiza uma tarefa existente.
    """
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )

    update_data = task.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)

    db.commit()
    db.refresh(db_task)
    return db_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
        task_id: int,
        db: Session = Depends(get_db),
        _=Depends(verify_token)
):
    """
    Remove uma tarefa existente.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )

    db.delete(task)
    db.commit()
    return None
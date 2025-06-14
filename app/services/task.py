from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

def get_task(db: Session, task_id: int, user_id: int):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == user_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task

def get_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Task).filter(Task.owner_id == user_id).offset(skip).limit(limit).all()

def create_task(db: Session, task: TaskCreate, user_id: int):
    db_task = Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task: TaskUpdate, user_id: int):
    db_task = get_task(db, task_id, user_id)
    update_data = task.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int, user_id: int):
    db_task = get_task(db, task_id, user_id)
    db.delete(db_task)
    db.commit()
    return {"message": "Tarefa deletada com sucesso"}
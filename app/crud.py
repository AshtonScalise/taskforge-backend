from sqlalchemy.orm import Session
from app.models import User, Project, Task
from app.schemas import UserCreate, ProjectCreate, TaskCreate
from app.auth import get_password_hash

def create_user(db: Session, user: UserCreate):
    hashed_pw = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_project(db: Session, project: ProjectCreate, owner_id: int):
    db_project = Project(**project.dict(), owner_id=owner_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_projects_by_user(db: Session, user_id: int):
    return db.query(Project).filter(Project.owner_id == user_id).all()


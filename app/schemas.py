from pydantic import BaseModel, EmailStr
from typing import Optional
import enum

class TaskStatus(str, enum.Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

# Auth
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = {
        "from_attributes": True,
    }

class Token(BaseModel):
    access_token: str
    token_type: str

# Project
class ProjectCreate(BaseModel):
    name: str

class ProjectOut(ProjectCreate):
    id: int
    owner_id: int

    model_config = {
        "from_attributes": True,
    }

# Task
class TaskCreate(BaseModel):
    title: str
    status: Optional[TaskStatus] = TaskStatus.todo
    project_id: int

class TaskOut(TaskCreate):
    id: int

    model_config = {
        "from_attributes": True,
    }

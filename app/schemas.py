from pydantic import BaseModel, EmailStr
from typing import Optional
import enum


# --- Auth / Token ---
class Token(BaseModel):
    access_token: str
    token_type: str


# --- User ---
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    team_id: Optional[int] = None

    model_config = {
        "from_attributes": True,
    }


# --- Team ---
class TeamCreate(BaseModel):
    name: str

class TeamOut(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True,
    }


# --- Project ---
class ProjectCreate(BaseModel):
    name: str

class ProjectOut(ProjectCreate):
    id: int
    owner_id: int
    team_id: Optional[int] = None

    model_config = {
        "from_attributes": True,
    }


# --- Task ---
class TaskStatus(str, enum.Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

class TaskCreate(BaseModel):
    title: str
    status: Optional[TaskStatus] = TaskStatus.todo
    project_id: int

class TaskOut(TaskCreate):
    id: int

    model_config = {
        "from_attributes": True,
    }

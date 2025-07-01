from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, models, crud, auth
from app.dependencies import get_db

router = APIRouter(prefix="/projects", tags=["projects"])

@router.post("/", response_model=schemas.ProjectOut)
def create_project(
    project: schemas.ProjectCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    return crud.create_project(db, project, current_user.id)

@router.get("/", response_model=list[schemas.ProjectOut])
def get_user_projects(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    return crud.get_projects_by_user(db, current_user.id)

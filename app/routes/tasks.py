from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, models, crud, auth
from app.dependencies import get_db

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=schemas.TaskOut)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    return crud.create_task(db, task, user_id=current_user.id)


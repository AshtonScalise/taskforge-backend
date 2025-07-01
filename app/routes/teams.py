from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, models, auth
from app.dependencies import get_db

router = APIRouter(prefix="/teams", tags=["teams"])


@router.post("/", response_model=schemas.TeamOut)
def create_team(
    team: schemas.TeamCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    existing = db.query(models.Team).filter(models.Team.name == team.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Team name already exists")

    new_team = models.Team(name=team.name)
    db.add(new_team)
    db.commit()
    db.refresh(new_team)

    # Assign user to this new team
    current_user.team_id = new_team.id
    db.commit()
    db.refresh(current_user)

    return new_team


@router.get("/me", response_model=schemas.TeamOut)
def get_my_team(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    team = db.query(models.Team).filter(models.Team.id == current_user.team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

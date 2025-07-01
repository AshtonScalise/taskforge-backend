from __future__ import annotations
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import models, schemas, crud, auth
from app.database import Base, engine
from app.dependencies import get_db

# Import modular auth router
from app.routes import all_routers

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# --- Mount Modular Routers ---
for router in all_routers:
    app.include_router(router)


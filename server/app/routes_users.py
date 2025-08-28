from typing import List
from datetime import datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .database import get_db
from .models import User

class UserCreate(BaseModel):
    name: str

class UserOut(BaseModel):
    id: int
    name: str
    created_at: datetime

    # Pydantic v2: allow building model from ORM instance
    model_config = {"from_attributes": True}

router = APIRouter()

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    obj = User(name=user.name)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/", response_model=List[UserOut])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(User).offset(skip).limit(limit).all()

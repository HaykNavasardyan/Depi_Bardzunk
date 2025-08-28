from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from database import get_db
from app.models import User

router = APIRouter(prefix="/users", tags=["users"])


class UserCreate(BaseModel):
    name: str


class UserResponse(BaseModel):
    id: int
    name: str
    created_at: str

    class Config:
        from_attributes = True


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user"""
    db_user = User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/", response_model=List[UserResponse])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List all users with pagination"""
    users = db.query(User).offset(skip).limit(limit).all()
    return users

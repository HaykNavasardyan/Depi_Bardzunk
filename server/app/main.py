from fastapi import FastAPI

from .database import engine
from .models import Base
from .routes_users import router as users_router
import os


if os.getenv("ENABLE_CREATE_ALL", "0") == "1":
    Base.metadata.create_all(bind=engine)


app = FastAPI(title="Depi Bardzunk API")

# Dev/test convenience: ensure tables exist (migrations still recommended)
Base.metadata.create_all(bind=engine)

@app.get("/", tags=["health"])
def root():
    return {"message": "Welcome to Depi Bardzunk API"}

@app.get("/health", tags=["health"])
def health():
    return {"ok": True}

app.include_router(users_router, prefix="/users", tags=["users"])

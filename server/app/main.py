from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.routes_users import router as users_router
from database import engine
from app.models import Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Depi Bardzunk API",
    description="FastAPI backend for Depi Bardzunk",
    version="0.1.0"
)

# Include routers
app.include_router(users_router)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"ok": True}

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to Depi Bardzunk API"}

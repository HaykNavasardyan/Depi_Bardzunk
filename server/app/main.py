from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Depi Bardzunk API",
    description="FastAPI backend for Depi Bardzunk",
    version="0.1.0"
)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"ok": True}

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to Depi Bardzunk API"}

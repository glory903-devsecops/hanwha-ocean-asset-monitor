from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import os

from . import models, database

# Initialize Database
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Shipyard Integrated Asset & IoT Monitoring API",
    description="Enterprise-grade API for Hanwha Ocean Smart Yard IT/OT Monitoring",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Hanwha Ocean AX Command Center API is Online", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": os.urandom(4).hex()} # Simple dynamic check

# Placeholder for Asset API
@app.get("/api/v1/assets")
async def get_assets(db: Session = Depends(database.get_db)):
    assets = db.query(models.Asset).all()
    return assets

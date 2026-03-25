from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import os

from . import models, database, schemas

# Initialize Database
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Shipyard Integrated Asset & IoT Monitoring API",
    description="Enterprise-grade API for Hanwha Ocean Smart Yard IT/OT Monitoring. \n\n*Note: Click 'Try it out' and 'Execute' to see the actual database data.*",
    version="1.0.1"
)

@app.get("/", tags=["Initial"])
async def root():
    return {
        "message": "Hanwha Ocean AX Command Center API is Online", 
        "status": "ready",
        "documentation": "/docs"
    }

@app.get("/health", tags=["Initial"])
async def health_check():
    return {"status": "healthy", "timestamp": os.urandom(4).hex()}

# Asset API with proper Schema
@app.get("/api/v1/assets", response_model=list[schemas.Asset], tags=["Asset Management"])
async def get_assets(db: Session = Depends(database.get_db)):
    """
    한화오션 야드 내 등록된 모든 IT/OT 자산 목록을 반환합니다.
    """
    assets = db.query(models.Asset).all()
    return assets

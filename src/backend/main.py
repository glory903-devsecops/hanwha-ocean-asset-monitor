from fastapi import FastAPI, Depends, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import os
from typing import List

from . import models, database, schemas

# Initialize Database
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Shipyard Integrated Asset & IoT Monitoring API",
    description="Enterprise-grade API for Hanwha Ocean Smart Yard IT/OT Monitoring. \n\n*Note: Click 'Try it out' and 'Execute' to see the actual database data.*",
    version="1.0.2"
)

# Enable CORS for local static file access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

# --- Asset Management Endpoints ---

@app.get("/api/v1/assets", response_model=List[schemas.Asset], tags=["Asset Management"])
async def get_assets(db: Session = Depends(database.get_db)):
    """한화오션 야드 내 등록된 모든 IT/OT 자산 목록을 반환합니다."""
    return db.query(models.Asset).all()

@app.post("/api/v1/assets", response_model=schemas.Asset, tags=["Asset Management"])
async def create_asset(asset: schemas.AssetCreate, db: Session = Depends(database.get_db)):
    """신규 자산을 CMDB에 등록합니다."""
    # Simple duplicate check
    existing = db.query(models.Asset).filter(models.Asset.asset_code == asset.asset_code).first()
    if existing:
        raise HTTPException(status_code=400, detail="Asset code already exists")
    
    db_asset = models.Asset(**asset.dict())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

@app.delete("/api/v1/assets/{asset_id}", tags=["Asset Management"])
async def delete_asset(asset_id: int, db: Session = Depends(database.get_db)):
    """특정 자산을 삭제합니다."""
    asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    db.delete(asset)
    db.commit()
    return {"message": f"Asset {asset_id} deleted successfully"}

@app.put("/api/v1/assets/{asset_id}/status", tags=["Asset Management"])
async def update_asset_status(asset_id: int, status: str = Body(..., embed=True), db: Session = Depends(database.get_db)):
    """자산의 상태(active/warning/critical)를 업데이트합니다."""
    asset = db.query(models.Asset).filter(models.Asset.id == asset_id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    asset.status = status
    db.commit()
    db.refresh(asset)
    return asset

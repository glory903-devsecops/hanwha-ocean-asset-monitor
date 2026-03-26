from fastapi import FastAPI, Depends, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import os
from typing import List

from . import database, schemas, service
from fastapi.staticfiles import StaticFiles

# Initialize Database
from . import models
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Hanwha Ocean AX Asset Monitoring API",
    version="1.1.1"
)

# Serve Frontend UIs
docs_path = os.path.join(os.getcwd(), "docs")
if os.path.exists(docs_path):
    app.mount("/ui", StaticFiles(directory=docs_path), name="ui")

# Also serve RPA folder for preview/portfolios
rpa_path = os.path.abspath(os.path.join(os.getcwd(), "..", "hanwha-ocean-rpa"))
if os.path.exists(rpa_path):
    app.mount("/rpa", StaticFiles(directory=rpa_path), name="rpa")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get Service
def get_asset_service(db: Session = Depends(database.get_db)):
    return service.AssetService(db)

@app.get("/", tags=["건강태 상태 확인"])
async def root():
    return {"message": "Hanwha Ocean AX API Online"}

@app.get("/api/v1/assets", response_model=List[schemas.Asset], tags=["자산 관리"])
async def read_assets(skip: int = 0, limit: int = 1000, asset_service: service.AssetService = Depends(get_asset_service)):
    return asset_service.get_assets(skip=skip, limit=limit)

@app.post("/api/v1/assets", response_model=schemas.Asset, tags=["자산 관리"])
async def add_asset(asset: schemas.AssetCreate, asset_service: service.AssetService = Depends(get_asset_service)):
    return asset_service.create_asset(asset)

@app.delete("/api/v1/assets/{asset_id}", tags=["자산 관리"])
async def remove_asset(asset_id: int, asset_service: service.AssetService = Depends(get_asset_service)):
    if not asset_service.remove_asset(asset_id):
        raise HTTPException(status_code=404, detail="자산을 찾을 수 없습니다.")
    return {"message": "자산이 안전하게 삭제되었습니다."}

@app.put("/api/v1/assets/{asset_id}/status", tags=["자산 관리"])
async def update_status(asset_id: int, status: str = Body(..., embed=True), asset_service: service.AssetService = Depends(get_asset_service)):
    asset = asset_service.change_status(asset_id, status)
    if not asset:
        raise HTTPException(status_code=404, detail="자산을 찾을 수 없습니다.")
    return asset

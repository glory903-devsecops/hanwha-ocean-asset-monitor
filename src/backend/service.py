from sqlalchemy.orm import Session
from .repository import AssetRepository
from . import schemas
from typing import List, Optional

class AssetService:
    def __init__(self, db: Session):
        self.repo = AssetRepository(db)

    def get_assets(self, skip: int = 0, limit: int = 1000) -> List[schemas.Asset]:
        return self.repo.get_all(skip=skip, limit=limit)

    def create_asset(self, asset_data: schemas.AssetCreate) -> schemas.Asset:
        # Business Logic: Check for duplicates
        if self.repo.get_by_code(asset_data.asset_code):
            from fastapi import HTTPException
            raise HTTPException(status_code=400, detail="이미 존재하는 자산 코드입니다.")
        return self.repo.create(asset_data)

    def remove_asset(self, asset_id: int) -> bool:
        return self.repo.delete(asset_id)

    def change_status(self, asset_id: int, status: str) -> Optional[schemas.Asset]:
        return self.repo.update_status(asset_id, status)

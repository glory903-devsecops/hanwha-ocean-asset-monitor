from sqlalchemy.orm import Session
from . import models, schemas
from typing import List, Optional

class AssetRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 1000) -> List[models.Asset]:
        return self.db.query(models.Asset).offset(skip).limit(limit).all()

    def get_by_code(self, asset_code: str) -> Optional[models.Asset]:
        return self.db.query(models.Asset).filter(models.Asset.asset_code == asset_code).first()

    def get_by_id(self, asset_id: int) -> Optional[models.Asset]:
        return self.db.query(models.Asset).filter(models.Asset.id == asset_id).first()

    def create(self, asset: schemas.AssetCreate) -> models.Asset:
        db_asset = models.Asset(**asset.dict())
        self.db.add(db_asset)
        self.db.commit()
        self.db.refresh(db_asset)
        return db_asset

    def delete(self, asset_id: int) -> bool:
        asset = self.get_by_id(asset_id)
        if asset:
            self.db.delete(asset)
            self.db.commit()
            return True
        return False

    def update_status(self, asset_id: int, status: str) -> Optional[models.Asset]:
        asset = self.get_by_id(asset_id)
        if asset:
            asset.status = status
            self.db.commit()
            self.db.refresh(asset)
            return asset
        return None

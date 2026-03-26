from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Any, Dict, List

class DeviceMetricBase(BaseModel):
    metric_type: str
    value: float
    unit: str

class DeviceMetric(DeviceMetricBase):
    id: int
    asset_id: int
    collected_at: datetime

    class Config:
        from_attributes = True

class AssetBase(BaseModel):
    asset_code: str
    name: str
    asset_type: str
    location: str
    status: str
    lifecycle_stage: str
    ip_address: Optional[str] = None
    metadata_json: Optional[Dict[str, Any]] = None

class AssetCreate(AssetBase):
    pass

class Asset(AssetBase):
    id: int
    created_at: datetime
    updated_at: datetime
    # metrics: List[DeviceMetric] = []

    class Config:
        from_attributes = True

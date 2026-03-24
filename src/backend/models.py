from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    asset_code = Column(String, unique=True, index=True)
    name = Column(String)
    asset_type = Column(String)  # Server, PC, IoT, Network, etc.
    location = Column(String)
    status = Column(String)      # active, warning, critical, inactive
    lifecycle_stage = Column(String) # procurement, deployment, operation, disposal
    ip_address = Column(String, nullable=True)
    serial_number = Column(String, nullable=True)
    eol_date = Column(DateTime, nullable=True)
    metadata_json = Column(JSON, nullable=True) # For flexible IoT properties
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    metrics = relationship("DeviceMetric", back_populates="asset")

class DeviceMetric(Base):
    __tablename__ = "device_metrics"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"))
    metric_type = Column(String) # cpu, memory, temp, vibration, etc.
    value = Column(Float)
    unit = Column(String)
    collected_at = Column(DateTime, default=datetime.datetime.utcnow)

    asset = relationship("Asset", back_populates="metrics")

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    action = Column(String)
    target_asset_id = Column(Integer, nullable=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    details = Column(String)

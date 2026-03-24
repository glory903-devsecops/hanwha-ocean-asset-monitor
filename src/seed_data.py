import sys
import os
from datetime import datetime, timedelta

# Add current directory to path
sys.path.append(os.path.dirname(__file__))

from backend import models, database

def seed_enterprise_assets():
    print("🌱 Seeding Enterprise IT/OT Assets...")
    
    # Ensure tables exist
    models.Base.metadata.create_all(bind=database.engine)
    
    db = database.SessionLocal()
    
    # Check if already seeded
    if db.query(models.Asset).first():
        print("💡 Database already contains assets. Skipping seed.")
        return

    # 1. IT Assets
    it_assets = [
        models.Asset(
            asset_code="SRV-GJ-SEC-01", name="Security Audit Server",
            asset_type="Server", location="Main Data Center", status="active",
            lifecycle_stage="operation", ip_address="192.168.1.10",
            eol_date=datetime.now() + timedelta(days=365*3)
        ),
        models.Asset(
            asset_code="NET-GJ-SW-CORE", name="Core Backbone Switch",
            asset_type="Network", location="Central Office", status="active",
            lifecycle_stage="operation", ip_address="192.168.1.1",
            metadata_json={"model": "Cisco 9500", "ports": 48}
        )
    ]
    
    # 2. IoT/OT Assets (Smart Yard)
    ot_assets = [
        models.Asset(
            asset_code="IOT-DOCK1-TEMP-01", name="Dock 1 Temperature Sensor",
            asset_type="IoT", location="Dock 1", status="warning",
            lifecycle_stage="operation", metadata_json={"sensor_type": "DHT22", "protocol": "MQTT"}
        ),
        models.Asset(
            asset_code="PLC-ASSY-ROBOT-04", name="Assembly Robot Controller",
            asset_type="IoT", location="Assembly Line B", status="active",
            lifecycle_stage="operation", metadata_json={"manufacturer": "Siemens", "model": "S7-1200"}
        )
    ]
    
    db.add_all(it_assets + ot_assets)
    db.commit()
    print(f"✅ Successfully seeded {len(it_assets) + len(ot_assets)} enterprise assets.")
    db.close()

if __name__ == "__main__":
    seed_enterprise_assets()

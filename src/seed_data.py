import sys
import os
from datetime import datetime, timedelta

# Add current directory to path
sys.path.append(os.path.dirname(__file__))

from backend import models, database

def seed_enterprise_assets():
    print("🌱 Seeding Realistic Hanwha Ocean IT/OT Assets...")
    
    # Ensure tables exist
    models.Base.metadata.create_all(bind=database.engine)
    
    db = database.SessionLocal()
    
    # Clear existing data for a clean update (Optional, but good for demo refresh)
    db.query(models.Asset).delete()
    
    # 1. IT Infrastructure (Enterprise Grade)
    it_assets = [
        models.Asset(
            asset_code="SRV-GJ-CMDB-01", name="AX Central CMDB Server",
            asset_type="Server", location="Main Data Center R-04", status="active",
            lifecycle_stage="operation", ip_address="10.20.1.10",
            metadata_json={"os": "RHEL 9.2", "specs": "64GB RAM, 2TB SSD"}
        ),
        models.Asset(
            asset_code="NET-GJ-CORE-01", name="Yard-Wide Backbone Switch",
            asset_type="Network", location="Network Hub Room", status="active",
            lifecycle_stage="operation", ip_address="10.20.0.1",
            metadata_json={"model": "Cisco Nexus 9000", "uptime": "342 days"}
        ),
        models.Asset(
            asset_code="SRV-GJ-SEC-GW", name="Security Gateway (DMZ)",
            asset_type="Security", location="Main Data Center R-01", status="active",
            lifecycle_stage="operation", ip_address="10.20.1.5",
            metadata_json={"firewall": "FortiGate 600F"}
        )
    ]
    
    # 2. Industrial OT & IoT (Shipyard Specific)
    ot_assets = [
        models.Asset(
            asset_code="ROB-WELD-DOCK1-05", name="Spider Welding Robot #5",
            asset_type="Industrial OT", location="Dock 1 Assembly Line", status="active",
            lifecycle_stage="operation", metadata_json={"manufacturer": "Hanwha Robotics", "axis": 6}
        ),
        models.Asset(
            asset_code="CRN-GOL-YARD5-01", name="Goliath Crane Controller",
            asset_type="Industrial OT", location="Yard 5 (Main)", status="active",
            lifecycle_stage="operation", metadata_json={"capacity": "900 tons", "plc_model": "Siemens S7-1500"}
        ),
        models.Asset(
            asset_code="SNS-ENV-DOCK2-42", name="Dock 2 Humidity/Temp Sensor",
            asset_type="IoT Node", location="Dock 2 (Bottom)", status="warning",
            lifecycle_stage="operation", metadata_json={"protocol": "LoRaWAN", "battery": "82%"}
        ),
        models.Asset(
            asset_code="PLC-AUTO-PIPE-12", name="Automated Pipe Cutting PLC",
            asset_type="Industrial OT", location="Pipe Shop #3", status="active",
            lifecycle_stage="operation", metadata_json={"firmware": "v2.4.1", "safety_status": "green"}
        )
    ]
    
    db.add_all(it_assets + ot_assets)
    db.commit()
    print(f"✅ Successfully seeded {len(it_assets) + len(ot_assets)} realistic enterprise assets.")
    db.close()

if __name__ == "__main__":
    seed_enterprise_assets()

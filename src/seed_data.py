import sys
import os
import random
import string
from datetime import datetime, timedelta

# Add current directory to path
sys.path.append(os.path.dirname(__file__))

from backend import models, database

def seed_enterprise_assets_large():
    print("🌱 Seeding High-Capacity Hanwha Ocean IT/OT Assets (1,000 Items across 100 Locations)...")
    
    # Ensure tables exist
    models.Base.metadata.create_all(bind=database.engine)
    
    db = database.SessionLocal()
    
    # Clear existing data
    db.query(models.Asset).delete()
    db.commit()
    
    # Generate 100 unique locations
    locations = []
    zones = ["Yard", "Dock", "Shop", "Lab", "Hub", "Zone"]
    for i in range(100):
        zone = random.choice(zones)
        sub_id = i + 1
        locations.append(f"{zone}-{sub_id:03d}")
    
    asset_types = {
        "Industrial OT": ["Spider Welding Robot", "Goliath Crane Controller", "Auto Cutting PLC", "Blast Machine Control"],
        "IoT Node": ["Humidity/Temp Sensor", "Vibration Node", "Noise Level Sensor", "Gas Detector"],
        "Server": ["AX CMDB Edge", "Monitoring Relay", "Security Gateway", "Data Historian"],
        "Network": ["Backbone Switch", "Wireless AP (Yard)", "Industrial Router"],
        "PC": ["Engineering Workstation", "QC Tablet", "Control Room PC"]
    }

    total_count = 0
    assets_per_loc = 10 # 100 locations * 10 assets = 1,000 assets
    
    for loc_idx, loc in enumerate(locations):
        for i in range(assets_per_loc):
            a_type = random.choice(list(asset_types.keys()))
            a_name_prefix = random.choice(asset_types[a_type])
            
            # Guaranteed uniqueness with loc_idx and asset index
            type_abbr = a_type[:3].upper()
            a_code = f"{type_abbr}-L{loc_idx:03d}-A{i:03d}"
            
            status = random.choices(["active", "warning", "critical"], weights=[92, 6, 2])[0]
            
            asset = models.Asset(
                asset_code=a_code,
                name=f"{a_name_prefix} - {loc} - {i:02d}",
                asset_type=a_type,
                location=loc,
                status=status,
                lifecycle_stage="operation",
                ip_address=f"192.168.{loc_idx}.{i+10}",
                eol_date=datetime.now() + timedelta(days=random.randint(60, 1800)),
                metadata_json={"fleet": "SmartYard-2026", "firmware": "v2.1.0"}
            )
            db.add(asset)
            total_count += 1
            
            if total_count % 100 == 0:
                db.commit()

    db.commit()
    print(f"✅ Successfully seeded {total_count} assets across {len(locations)} locations.")
    db.close()

if __name__ == "__main__":
    seed_enterprise_assets_large()

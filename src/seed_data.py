import sys
import os
import random
import string
from datetime import datetime, timedelta

# Add current directory to path
sys.path.append(os.path.dirname(__file__))

from backend import models, database

def seed_enterprise_assets_large():
    print("🌱 Seeding High-Capacity Hanwha Ocean IT/OT Assets (700+ Items)...")
    
    # Ensure tables exist
    models.Base.metadata.create_all(bind=database.engine)
    
    db = database.SessionLocal()
    
    # Clear existing data
    db.query(models.Asset).delete()
    db.commit()
    
    locations = [
        "제1도크 조립공장", "제2도크 (Bottom)", "제3도크 육상건조장", "제5야드 (Goliath)",
        "Pipe Shop #1", "Pipe Shop #2", "Pipe Shop #3", "Engine Room A", 
        "메인 데이터 센터 R-04", "본관 설계동 3F", "야드 네트워크 허브 01", "도장공장 C구역"
    ]
    
    asset_types = {
        "Industrial OT": ["Spider Welding Robot", "Goliath Crane Controller", "Auto Cutting PLC", "Blast Machine Control"],
        "IoT Node": ["Humidity/Temp Sensor", "Vibration Node", "Noise Level Sensor", "Gas Detector"],
        "Server": ["AX CMDB Edge", "Monitoring Relay", "Security Gateway", "Data Historian"],
        "Network": ["Backbone Switch", "Wireless AP (Yard)", "Industrial Router"],
        "PC": ["Engineering Workstation", "QC Tablet", "Control Room PC"]
    }

    total_count = 0
    for loc_idx, loc in enumerate(locations):
        for i in range(60):
            a_type = random.choice(list(asset_types.keys()))
            a_name_prefix = random.choice(asset_types[a_type])
            
            # Use location index (Lxx) and type (TYP) for guaranteed uniqueness
            type_abbr = a_type[:3].upper()
            a_code = f"{type_abbr}-L{loc_idx:02d}-{i:03d}"
            
            status = random.choices(["active", "warning", "critical"], weights=[90, 8, 2])[0]
            
            asset = models.Asset(
                asset_code=a_code,
                name=f"{a_name_prefix} - {i:03d}",
                asset_type=a_type,
                location=loc,
                status=status,
                lifecycle_stage="operation",
                ip_address=f"10.20.{loc_idx}.{i}",
                eol_date=datetime.now() + timedelta(days=random.randint(30, 2000)),
                metadata_json={"batch": "2026-Q1", "maintenance_cycle": "6 months"}
            )
            db.add(asset)
            total_count += 1
            
            if total_count % 100 == 0:
                db.commit()

    db.commit()
    print(f"✅ Successfully seeded {total_count} high-performance enterprise assets with unique codes.")
    db.close()

if __name__ == "__main__":
    seed_enterprise_assets_large()

import sys
import os
from sqlalchemy.orm import Session
from src.backend import models, database, schemas

def test_get_assets():
    db = next(database.get_db())
    try:
        assets = db.query(models.Asset).all()
        print(f"Successfully retrieved {len(assets)} assets from DB.")
        failures = 0
        for i, asset in enumerate(assets):
            try:
                schemas.Asset.model_validate(asset)
            except Exception as e:
                failures += 1
                print(f"FAILED at Index {i} (ID: {asset.id}): {e}")
                if failures >= 5: break
        if failures == 0:
            print("All assets serialized successfully!")
    except Exception as e:
        print(f"Query FAILED: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_get_assets()

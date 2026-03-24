import subprocess
import sys
import os

def run():
    # 1. Seed Data first
    print("Step 1: Initializing Database & Seed Data...")
    subprocess.run([r".\venv\Scripts\python.exe", r"src\seed_data.py"], check=True)
    
    # 2. Launch FastAPI with Uvicorn
    print("\nStep 2: Launching Hanwha Ocean AX Command Center API...")
    # Using uvicorn main:app from the backend folder
    # Note: --reload for development
    subprocess.run([r".\venv\Scripts\uvicorn.exe", "src.backend.main:app", "--host", "127.0.0.1", "--port", "8000", "--reload"])

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n👋 Server shutdown by user.")
    except Exception as e:
        print(f"\n❌ Execution Error: {e}")

# ⚓ Shipyard Integrated Asset & IoT Monitoring Dashboard
> **"AX Command Center for Hanwha Ocean Smart Yard"**

This project is an enterprise-grade **Unified IT/OT Asset Monitoring System** designed for the modern shipyard. It provides real-time visibility into IT infrastructure (Servers, Network) and Production OT/IoT devices (Sensors, PLCs, Robots), directly supporting Hanwha Ocean's 2030 Smart Yard Strategy.

## 🚀 Strategic Value Proposition (AX/DX)
- **IT/OT Convergence**: Break down silos between data centers and production docks.
- **Downtime Minimization**: Real-time status tracking and proactive failure monitoring.
- **Lifecycle Optimization**: Automated CMDB (Configuration Management Database) for ITAM/ITSM best practices.
- **RPA Integration**: Seamlessly bridge the gap between "detecting a failure" and "procuring a replacement" via automated tickets.

## 🛠 Tech Stack
- **Backend**: Python (FastAPI), SQLAlchemy (SQLite/PostgreSQL), Pydantic
- **Frontend**: React, Apache ECharts (Dynamic Industrial Visualization)
- **Data Protocols**: MQTT (IoT), SNMP (Network Infrastructure)
- **Architecture**: 3-Tier Web Application with RESTful API & JWT Security

## 📂 Project Structure
- `src/backend/`: FastAPI core, CMDB models, and database logic.
- `src/frontend/`: React components and industrial dashboard (ECharts).
- `src/seed_data.py`: Factory script to populate the system with realistic shipyard assets.
- `docs/`: Strategic planning documents (AX Strategy, BRD, SDD).

## 🏁 Quick Start (One-Click Demo)
1. **Initialize Environment**:
   ```powershell
   python -m venv venv
   ./venv/Scripts/pip install -r requirements.txt
   ```
2. **Launch System**:
   ```powershell
   python run_dev.py
   ```
3. **Explore Architecture**:
   Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the **Swagger UI** and interact with the Live IT/OT CMDB.

---
**Designed & Developed by Glory (AX/DevSecOps Engineer)**
*Bridging the gap between IT support and Smart Factory innovation.*

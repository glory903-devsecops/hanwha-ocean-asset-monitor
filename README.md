# 한화오션 AX 통합 자산 모니터링 시스템

[![Enterprise CI](https://github.com/glory903-devsecops/hanwha-ocean-asset-monitor/actions/workflows/python-app.yml/badge.svg)](https://github.com/glory903-devsecops/hanwha-ocean-asset-monitor/actions)
[![Live Demo](https://img.shields.io/badge/Live_Demo-View_Dashboard-FF6B00?style=for-the-badge&logo=airplayvideo)](https://glory903-devsecops.github.io/hanwha-ocean-asset-monitor/)
> **"스마트 야드를 위한 AX 커맨드 센터"**

한화오션 스마트 야드(Smart Yard) 2030 핵심 전략인 **AX(AI Transformation)**를 위한 엔터프라이즈급 자산 통합 모니터링 시스템입니다. 1,000대 이상의 IT/OT 자산을 실시간으로 관리하고 AI 기반 이상 징후를 탐지합니다.

> [!TIP]
> **준비된 3가지 포트폴리오 시연 방식** (Recruiter-Ready)
> 1. **실시간 서버 모드**: `python run_dev.py` 실행 시 실제 SQL DB 연동 (백엔드 역량 증명)
> 2. **오프라인 데모 모드**: 서버 없이 `index.html`만 열어도 1,000개 자산 자동 시뮬레이션 (간편 시연)
> 3. **웹 라이브 데모**: [GitHub Pages](https://glory903-devsecops.github.io/hanwha-ocean-asset-monitor/) (접속 즉시 확인 가능)

---

## 🖥️ UI Preview (미리보기)

### 1. 통합 모니터링 대시보드 (AI & RPA Dashboard)
![Dashboard Preview](docs/images/dashboard.png)
> **AI 예측 기반의 정비 알람 및 RPA 자동화 로그를 실시간으로 시각화한 메인 화면입니다.**

### 2. 자산 인벤토리 관리 (CMDB Management)
![Management Preview](docs/images/management.png)
> **한화오션 거제 야드 내 모든 IT/OT 자산의 라이프사이클을 관리하는 인터페이스입니다.**

---

## 🚀 전략적 가치 제안 (AX/DX)
- **IT/OT 융합**: 데이터 센터와 생산 도크 간의 정보 사일로(Silo)를 제거합니다.
- **다운타임 최소화**: 실시간 상태 추적 및 선제적 장애 모니터링을 통한 가동률 극대화.
- **라이프사이클 최적화**: ITAM/ITSM 베스트 프랙티스를 적용한 자동화된 CMDB(구성 관리 데이터베이스).
- **RPA 통합 연계**: 장애 감지부터 부품 조달 및 티켓 발행까지 이어지는 프로세스 자동화의 기반.

## 기술 스택
- **Backend**: Python (FastAPI), SQLAlchemy (SQLite/PostgreSQL), Pydantic
- **Frontend**: React, Apache ECharts (역동적인 산업용 시각화)
- **데이터 프로토콜**: MQTT (IoT), SNMP (네트워크 인프라)
## 🛠 시스템 아키텍처 (Clean Architecture 적용)

본 프로젝트는 유지보수성과 확장성을 극대화하기 위해 **SOLID 원칙**과 **Clean Architecture** 패턴으로 리팩토링되었습니다.

- **API Layer (Controller)**: FastAPI를 통한 요청 처리 및 스태틱 UI 서버 (Static UI Serving)
- **Service Layer (Business Logic)**: 자산 등록 규칙, 중복 검사 등 비즈니스 로직 담당
- **Repository Layer (Data Access)**: SQLAlchemy를 통한 데이터베이스 추상화 (SQLAlchemy ORM)
- **Domain Layer (Entities)**: Pydantic을 활용한 데이터 모델 규격화 (Pydantic Schemas)

## 📦 설치 및 실행 방법

1. **가상환경 설정 및 패키지 설치**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **서버 실행 (uvicorn)**
   ```powershell
   python run_dev.py
   ```
   *접속 정보: http://127.0.0.1:8000/ui/index.html*

3. **데이터 초기화 (1,000개 자산)**
   ```powershell
   python src/seed_data.py
   ```

## 📊 기술 스택
- **Backend**: Python 3.10+, FastAPI, SQLAlchemy, Pydantic, Uvicorn
- **Frontend**: Vanilla JS (ES6+), ECharts, CSS Grid/Flexbox
- **Database**: SQLite (Development) / PostgreSQL (Ready)

## 프로젝트 구조 및 문서 저장소 (Documentation)
이 프로젝트는 단순 개발을 넘어 기획부터 검증까지의 전 과정이 엔터프라이즈급으로 설계되었습니다.

* **[문서 저장소 (Docs Directory)](./docs/README.md)**: 기획서, 전략 가이드 등의 상세 문서가 위치한 곳입니다.
  - [01. 개발 기획서 (AX 전략 기반)](./docs/01_개발_기획서_AX_통합_모니터링.md): 한화오션 JD 분석 및 시스템 아키텍처 기획안.
  - [02. 경영진 전략 가이드](./docs/02_경영진_위한_전략_가이드.md): IT 지원 실무 경험을 바탕으로 한 비즈니스 가치 제안서.

---

- `src/backend/`: FastAPI 코어, CMDB 모델 및 데이터베이스 로직.
- `src/frontend/`: React 컴포넌트 및 산업용 대시보드(ECharts).
- `src/seed_data.py`: 실제 조선소 자산 데이터를 생성하는 팩토리 스크립트.
- `docs/`: 전략 기획 문서 (AX 전략, BRD, SDD).

## 🏁 빠른 시작 (데모 실행)
1. **환경 초기화**:
   ```powershell
   python -m venv venv
   ./venv/Scripts/pip install -r requirements.txt
   ```
2. **시스템 실행**:
   ```powershell
   python run_dev.py
   ```
3. **아키텍처 탐색**:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)에 접속하여 **Swagger UI**를 통해 IT/OT CMDB 실시간 데이터를 확인하십시오.

## 📊 시스템 검증 결과 (Verification Results)
유닛 테스트 및 데이터 검증을 통해 확인된 핵심 성과입니다:

- **통합 자산 관리 (Total Assets)**: 현재 **1,000개**의 핵심 엔터프라이즈 자산 실시간 추적 중.
  - **IT 인프라**: 서버, 네트워크, 보안 게이트웨이 등 3개 자산.
  - **OT/IoT 스마트 야드**: 용접 로봇, 골리앗 크레인, 환경 센서 등 4개 자산.
- **실시간 장애 감지**: **Dock 2 환경 센서(SNS-ENV-DOCK2-42)**의 이상 수치를 성공적으로 감지하여 경고(Warning) 상태로 분류.
- **AX 기반 의사결정 지원**: 
  - IT와 생산 현장(OT) 자산을 하나의 화면에서 통합이것으로 포트폴리오의 시각적 완성도까지 완벽하게 마무리되었습니다. 한화오션에서의 좋은 결과를 다시 한번 진심으로 응원합니다.

기획 및 개발: Glory (AX/DevSecOps 엔지니어)
*IT 지원과 스마트 팩토리 혁신 사이의 가교(Bridge) 역할을 수행합니다.*

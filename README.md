# Banking Operations & System Health Dashboard

An end-to-end simulated banking operations project demonstrating SQL, Python, business analysis, workflow design and Power BI.

## Objective
Identify potentially high-risk account behaviour, validate alerts, route exceptions through a simulated escalation workflow and provide executive visibility of financial and system health.

## Architecture
Banking Data → SQL → Python Validation/Risk Detection → Risk Alert Queue → Operations Workflow → Power BI → Executive Dashboard → Interest Rate What-If

## Technology
SQL/SQLite • Python • Power BI • DAX • Mermaid/SVG • Git/GitHub

## Repository
- `data/` synthetic CSVs
- `sql/` schema, seed data, views and detection queries
- `python/` validation, risk detection and escalation workflow
- `powerbi/` model, DAX and build guide
- `architecture/` architecture/process diagrams
- `documentation/` BRD, user stories, test cases and data dictionary
- `outputs/` generated alerts/escalations

## Quick start
```bash
python python/run_pipeline.py
```

The supplied `banking_operations.db` is already populated. SQL files can rebuild it from scratch.

## Power BI
Load the CSVs or SQLite database and follow the files in `powerbi/`.

Recommended pages:
1. Executive Risk Overview
2. Operational System Health
3. Risk & Escalation Detail
4. Interest Rate What-If Analysis

## Portfolio story
Business problem → Requirements → Data model → SQL → Python → Workflow → Power BI → Executive insight

## Disclaimer
All data is synthetic. The rules are educational portfolio simulations and are not production banking fraud, AML, credit or affordability models.

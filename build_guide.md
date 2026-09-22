# Power BI Build Guide
1. Load the CSVs or SQLite database.
2. Create DimDate from 2024-01-01 to 2026-09-20.
3. Build the star schema in data_model.md.
4. Add DAX measures from DAX_measures.txt.
5. Create What-If parameter `Interest Rate Parameter`: -1.00% to +1.50%, step 0.50%.
6. Pages: Executive Risk Overview; Operational System Health; Risk & Escalation Detail; Interest Rate What-If.
7. KPI cards: high-risk alerts, loan exposure, open alerts, average resolution time, validation success, SLA breaches.
8. Use drill-through for alert/customer detail.
All models and rules are synthetic portfolio demonstrations.

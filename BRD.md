# Business Requirements Document
## Banking Operations & System Health Dashboard

### Purpose
Create a simulated end-to-end banking operations monitoring solution that identifies potentially high-risk customer/account activity and provides operational and executive visibility.

### Stakeholders
Banking Operations Manager; Risk Analyst; Credit Operations; Financial Crime Operations; Data/BI Analyst; Senior Banking Executive; Technology/Application Support.

### Functional requirements
FR-01 Load customer, account, loan, payment and transaction data into SQL.
FR-02 Validate key fields, duplicates and record completeness.
FR-03 Detect consecutive missed payments.
FR-04 Detect unusual recent debit/overdraft activity.
FR-05 Detect rapid cross-border transaction activity.
FR-06 Calculate configurable risk scores.
FR-07 Create risk alerts and assign an operational team.
FR-08 Create simulated escalation records.
FR-09 Track validation/resolution times.
FR-10 Provide Power BI executive KPIs.
FR-11 Provide an interest-rate What-If parameter.
FR-12 Support filtering and alert drill-through.

### Non-functional requirements
Reproducible synthetic data; modular Python scripts; indexed SQL keys; traceable workflow; documented assumptions/tests.

### Assumptions
All data and rules are synthetic and illustrative. They are not production credit, AML, fraud or affordability models.
